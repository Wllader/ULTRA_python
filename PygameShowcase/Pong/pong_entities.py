import pygame as pg, numpy as np
from abc import ABC
from enum import Enum, auto
from game_controller import GameController
from spritesheet_sr_fc import SpriteSheet

class MovingDirection(Enum):
    Horizontal = 0
    Vertical = 1

class PongEntity(pg.sprite.Sprite, ABC):
    def __init__(
            self,
            screen:pg.Surface,
            size:np.ndarray,
            init_center_pos:np.ndarray,
            speed:np.ndarray,
            color:np.ndarray,
            sprite_sheet:SpriteSheet = None
        ):
        super().__init__()

        self.gc = GameController()
        
        self.sheet = sprite_sheet if sprite_sheet else None
        self.screen = screen
        self._image = pg.Surface(size)
        if sprite_sheet is not None:
            self._image = self.sheet.frame

        self.color = color
        self.rect = self._image.get_frect(center=init_center_pos)
        self.speed = speed

        self.old_rect = self.rect.copy()
        self.size_changed = True

    @property
    def dt(self):
        return self.gc.dt
    
    @property
    def screen_center(self):
        return np.array([
                self.screen.get_width(),
                self.screen.get_height()
            ]) / 2

    @property
    def image(self):
        if self.sheet is None:
            self._image.fill(self.color)
        else:
            self._image = self.sheet.frame #new
            if self.size_changed:
                self.rect = self._image.get_frect(center=self.rect.center)
                self.size_changed = False
        return self._image
    

    def update(self):
        self.window_correction()

    def window_correction(self):
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > (h := self.screen.get_height()):
            self.rect.bottom = h

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > (w := self.screen.get_width()):
            self.rect.right = w

    @staticmethod
    def intersect_implicit_func(vector:np.ndarray, location:np.ndarray, axis_x) -> float:
        "This implementation uses Implicit function of a line"
        # ax + by + c = 0
        # c = -(ax + by): (-b, a) = ball_speed, (x, y) = ball_center
        # y = (ax + c)/(-b): (-b, a) = ball_speed, x = axis_x
        normal = vector.copy()[::-1]
        normal[0] *= -1

        c = -np.dot(normal, location)
        y = (normal[0] * axis_x + c)/(-normal[1])
        return y
    
    @staticmethod
    def intersect(vector:np.ndarray, location:np.ndarray, axis_x) -> float:
        "This implementation uses parametric description of a line"
        # x' = x + u1*t -> t = (x' - x)/u1 [where x' == axis_x]
        # y' = y + u2*t
        t = (axis_x - location[0])/vector[0]
        y = location[1] + vector[1]*t

        return y
    
    @staticmethod
    def bound(y:float, lower_bound:int, upper_bound:int) -> float:
        span = upper_bound - lower_bound

        pos = (y - lower_bound) % (2*span)
        if pos > span:
            pos = 2*span - pos

        return pos + lower_bound

    @staticmethod
    def _bound(y:float, lower_bound:int, upper_bound:int) -> float:
        "This implementation is inefficient!"
        if y >= lower_bound and y <= upper_bound:
            return y
        
        if y < lower_bound:
            y0 = np.abs(lower_bound - y)
            return PongEntity.bound(y + 2*y0, lower_bound, upper_bound)
        
        if y > upper_bound:
            y0 = np.abs(upper_bound - y)
            return PongEntity.bound(y - 2*y0, lower_bound, upper_bound)
        

    @staticmethod
    def ccd(start:np.ndarray, end:np.ndarray, axis:float, index:int) -> tuple[np.ndarray, float]:
        # a := start, b := end
        # (1-t)*a + t*b = axis
        # (1-t)*a_y + t*b_y = axis_y
        # -> t = (axis-a)/(b-a)
        t = ((axis - start)/(end - start))[index]
        return (1-t)*start + t*end, t
    
    def ccd_collison(self, group:pg.sprite.Group) -> tuple[np.ndarray, float, MovingDirection] | None:
        if len(group) == 0: return None
        a = np.array(self.old_rect.center)
        b = np.array(self.rect.center)
        u = b - a

        dx = u[0]
        dy = u[1]

        results = []
        for sprite in group:
            sprite:pg.sprite.Sprite
            r = sprite.rect.inflate(*self.rect.size)
            r_sides = [
                (r.topleft, r.topright, MovingDirection.Vertical) if dy > 0 else
                (r.bottomright, r.bottomleft, MovingDirection.Vertical),
                (r.topright, r.bottomright, MovingDirection.Horizontal) if dx < 0 else
                (r.bottomleft, r.topleft, MovingDirection.Horizontal)
            ]
            result_ts = []
            for c, d, m in r_sides:
                c = np.array(c)
                d = np.array(d)

                At = np.array((a-c, d-c)).T
                B = np.array((a-b, d-c)).T

                t = np.linalg.det(At) / np.linalg.det(B)
                if t < 0 or t > 1 or np.isnan(t): continue

                As = np.array((a-b, a-c)).T
                s = np.linalg.det(As) / np.linalg.det(B)
                if s < 0 or s > 1 or np.isnan(s): continue

                result_ts.append((t, m))

            if not result_ts: continue
            t, direction = min(result_ts, key=lambda _t: _t[0])
            col = a + t*u
            results.append((col, t, direction))

        res = None
        if results:
            res = min(results, key=lambda res: res[1])

        return res


class PongPlayer(PongEntity):
    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.rect.y -= self.speed[1] * self.dt

        if keys[pg.K_s]:
            self.rect.y += self.speed[1] * self.dt

        self.window_correction()

class PongBot(PongEntity):
    def __init__(self, screen, size, init_center_pos, speed, color, sprite_sheet:SpriteSheet):
        super().__init__(screen, size, init_center_pos, speed, color, sprite_sheet)

        self.ball:PongEntity = None

    def update(self):
        if self.ball is None: return
        if self.ball_moving_towards_me():
            self.drift_towards(self.ball.rect.center)
        else:
            self.drift_towards(self.screen_center)

        self.window_correction()

    def drift_towards(self, center:np.ndarray):
        if self.rect.centery > center[1]:
            self.rect.y -= self.speed[1] * self.dt
        elif self.rect.centery < center[1]:
            self.rect.y += self.speed[1] * self.dt

    def ball_moving_towards_me(self) -> bool:
        ball_now = self.ball.rect.center
        ball_next = ball_now + self.ball.speed * self.dt

        dist_now = np.abs(self.rect.centerx - ball_now[0])
        dist_next = np.abs(self.rect.centerx - ball_next[0])

        return dist_next < dist_now


class PongBotAdvanced(PongBot):
    def __init__(self, screen, size, init_center_pos, speed, color, sprite_sheet):
        super().__init__(screen, size, init_center_pos, speed, color, sprite_sheet)

        self.target = None

    def _predict_ball_pos(self):
        ball_half_width = self.ball.rect.width / 2
        paddle_axis = self.rect.right + ball_half_width if self.ball.speed[0] < 0 else self.rect.left - ball_half_width

        y = self.intersect(self.ball.speed, self.ball.rect.center, paddle_axis)
        y = self.bound(y, 0, self.screen.get_height())

        return y

    def update(self):
        if self.ball_moving_towards_me():
            y = self._predict_ball_pos()
            target = np.array([0, y], dtype=int)

        else:
            target = self.screen_center.astype(int)

        if self.target is None or np.abs(self.target[1] - target[1]) >= self.rect.height / 2:
            self.target = target

        self.drift_towards(self.target)
        self.window_correction()
        self.old_rect = self.rect.copy()


class PongBall(PongEntity):
    def __init__(self, screen, size, init_center_pos, speed, color, sprite_sheet:SpriteSheet):
        super().__init__(screen, size, init_center_pos, speed, color, sprite_sheet)

        self.g_bounce = pg.sprite.Group()

    @property
    def image(self):
        if self.sheet is None:
            pg.draw.ellipse(self._image, self.color, self._image.get_frect())
        else:
            self._image = self.sheet.frame
            if self.size_changed:
                self.rect = self._image.get_frect(center=self.rect.center)
                self.size_changed = False
        return self._image


    def update(self):
        self.rect.center += self.speed * self.dt
        self.handle_collisions_continuous()

        self.window_correction()

        self.old_rect = self.rect.copy()

    def handle_collisions(self, direction:MovingDirection): #obsolete
        if (o := self.rect.collideobjects(list(self.g_bounce))) and o is not None:
            o:PongEntity

            self.color = o.color

            if direction == MovingDirection.Horizontal:
                dx = self.rect.x - self.old_rect.x

                if dx > 0: # We were moving RIGHT:
                    self.bounce_edge(o.rect.left - self.rect.width / 2, 0)
                elif dx < 0: # We were moving LEFT:
                    self.bounce_edge(o.rect.right + self.rect.width / 2, 0)

            if direction == MovingDirection.Vertical:
                dy = self.rect.y - self.old_rect.y

                if dy > 0: # We were moving DOWN:
                    self.bounce_edge(o.rect.top - self.rect.height / 2, 1)
                elif dy < 0: # We were moving UP:
                    self.bounce_edge(o.rect.bottom + self.rect.height / 2, 1)

    def handle_collisions_continuous(self):
        if (ctd := self.ccd_collison(self.g_bounce)) and ctd is not None:
            c, t, d = ctd

            self.bounce(c, t, d.value)


    
    def window_correction(self):
        super().window_correction()

        if self.rect.top <= 0:
            self.bounce_edge(0 + self.rect.height / 2, 1)
        elif self.rect.bottom >= (h := self.screen.get_height()):
            self.bounce_edge(h - self.rect.height / 2, 1)

        #? Respawn
        if (l := self.rect.left <= 0) or self.rect.right >= self.screen.get_width():
            self.rect.center = np.array([
                self.screen_center[0],
                np.random.randint(0, self.screen.get_height())
            ])
            self.color = np.ones(3, dtype=np.uint8) * 255
            self.speed[0] *= -1

            #? Scoring
            # self.gc.score(0) if not l else self.gc.score(1)
            self.gc.score(1) if l else self.gc.score(0)


    def bounce_edge(self, axis:float, index:int):
        c, t = self.ccd(
            np.array(self.old_rect.center), np.array(self.rect.center),
            axis, index
        )

        self.speed[index] *= -1
        self.rect.center = c + self.speed * (1-t) * self.dt

    def bounce(self, c, t, index:int):
        self.speed[index] *= -1
        self.rect.center = c + self.speed * (1-t) * self.dt
