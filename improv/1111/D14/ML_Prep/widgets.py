import pygame as pg, numpy as np
from enum import Enum, auto
from typing import Callable
from game_controller import GameController
from tween import Tween
from scipy.ndimage import center_of_mass, shift

GREY = np.ones(3, dtype=np.uint8)
WHITE = GREY * 255
BLACK = GREY * 0
NONE = np.zeros(4, dtype=np.uint8)

class ClickState(Enum):
    RELEASED = auto()
    CLICKED = auto()
    HELD = auto()
    MISSED = auto()


class Widget(pg.sprite.Sprite):
    def __init__(self, screen:pg.Surface, pos:tuple[int], size:tuple[int]):
        super().__init__()

        self.gc = GameController()
        
        self.screen = screen
        self._rect = pg.Rect(*pos, *size)
        self._image = pg.Surface(size)

        self.mouse_held = np.zeros(3, dtype=bool)
        self.enabled = True

    def update(self, event:pg.event.Event=None):
        super().update()

    @property
    def dt(self):
        return self.gc.dt

    @property
    def rect(self):
        return self._rect
    
    @property
    def image(self):
        return self._image
    
    @property
    def size(self):
        return np.array(self._rect.size)
    
    @property
    def position(self):
        return np.array(self._rect.topleft)
    
    @property
    def center(self):
        return np.array(self._rect.center)
    

    def align_center(self, other:pg.Surface) -> np.ndarray:
        a = np.array(self.size)
        b1 = np.array(other.size)
        b2 = np.array(other.get_bounding_rect().size)
        b = (b1+b2)/2
        return np.abs(a-b)/2

    
    def click(self, button:int) -> ClickState:
        p = pg.mouse.get_pressed()[button]
        h = self.mouse_held[button]
        c = self.hover()

        if p and not h and c:
            self.mouse_held[button] = True
            return ClickState.CLICKED
        elif p and h and c:
            return ClickState.HELD
        elif not p and h:
            self.mouse_held[button] = False
            return ClickState.RELEASED
        elif p and not h and not c:
            return ClickState.MISSED
        
    def hover(self) -> bool:
        return self._rect.collidepoint(pg.mouse.get_pos())
    
    def disable(self): self.enabled = False
    def enable(self): self.enabled = True


class Label(Widget):
    def __init__(self, screen, pos, size, text:str, font=None, fg:tuple[int] = WHITE, bg:tuple[int] = NONE):
        super().__init__(screen, pos, size)

        self.text = text
        self.font:pg.font.Font = font if font is not None else pg.font.SysFont("Calibri", self.size[1])
        self.fg = fg
        self.bg = bg

    @property
    def image(self):
        label = self.font.render(self.text, True, self.fg, self.bg)
        pos = self.align_center(label)
        self._image.blit(label, pos)
        return self._image

class Button(Widget):
    def __init__(self, screen, pos, size, text:str, font=None, fg:tuple[int] = BLACK, bg:tuple[int] = WHITE, command=lambda: print("Clicked!")):
        super().__init__(screen, pos, size)
        
        self.text = text
        self.font:pg.font.Font = font if font is not None else pg.font.SysFont("Calibri", self.size[1]//2)
        self.fg = fg
        self.bg = bg
        self.command = command

    @property
    def image(self):
        self._image.fill(self.bg)
        label = self.font.render(self.text, True, self.fg)
        pos = self.align_center(label)
        self._image.blit(label, pos)

        if self.mouse_held[0]:
            self._image.fill(GREY * 150, special_flags=pg.BLEND_RGBA_MULT)
        elif self.hover():
            self._image.fill(GREY * 200, special_flags=pg.BLEND_RGBA_MULT)

        return self._image
    
    def update(self, event=None):
        super().update(event)

        if self.click(0) == ClickState.CLICKED:
            self.command()


class Entry(Widget):
    def __init__(self, screen, pos, size, font=None, fg:tuple[int] = WHITE, bg:tuple[int] = GREY*28, default_text:str="", tooltip_text:str=""):
        super().__init__(screen, pos, size)
        
        self.font = font if font is not None else pg.font.SysFont("Calibri", self.size[1]//2)
        self.fg = fg
        self.bg = bg
        self.text = default_text
        self.tooltip = tooltip_text

        self.selected = False

    @property
    def image(self):
        self._image.fill(self.bg)
        if self.has_text():
            label = self.font.render(self.text, True, self.fg)
        else:
            label = self.font.render(self.tooltip, True, self.fg * .6)

        pos = self.align_center(label)
        self._image.blit(label, pos)

        if self.selected:
            self._image.fill(GREY * 60, special_flags=pg.BLEND_RGBA_ADD)
        if self.hover():
            self._image.fill(GREY * 200, special_flags=pg.BLEND_RGBA_MULT)

        return self._image

    def has_text(self) -> bool:
        return self.text != ""
    
    def update(self, event:pg.event.Event=None):
        super().update(event)

        match self.click(0):
            case ClickState.CLICKED:
                self.selected = True
            case ClickState.MISSED:
                self.selected = False

        if self.selected and event and event.type == pg.KEYDOWN:
            match event.key:
                case pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                case pg.K_RETURN:
                    self.selected = False
                case _:
                    self.text += event.unicode


class CheckBox(Widget):
    def __init__(self, screen, pos, size, checked=False):
        super().__init__(screen, pos, size)

        self.checked = checked

    @property
    def image(self):
        pg.draw.rect(self._image, WHITE, (0, 0, *self.size), 1)

        if self.checked:
            pg.draw.lines(self._image, WHITE, False, [(0, 0), (self.size[0] / 2, self.size[1]), (self.size[0], 0)])

        if self.mouse_held[0]:
            pg.draw.line(self._image, WHITE, (0, 0), (self.size[0] / 2, self.size[1]))
            self._image.fill(GREY * 150, special_flags=pg.BLEND_RGBA_MULT)
        elif self.hover():
            self._image.fill(GREY * 200, special_flags=pg.BLEND_RGBA_MULT)


        return self._image

    def get(self):
        return self.checked

    def update(self, event=None):
        super().update(event)

        if self.click(0) == ClickState.RELEASED:
            self.checked = not self.checked


class Canvas(Widget):
    def __init__(self, screen, pos, size, resolution=(28, 28)):
        super().__init__(screen, pos, size)

        self.resolution = np.array(resolution)
        self.pixels = np.zeros((*self.resolution, ), dtype=np.uint8)

        self.cell_size = self.size / self.resolution
        self.dirty = True
        self._last_pos = None


    @property
    def image(self):
        """Vrátí aktuální Surface (kompatibilní s Group.draw())."""
        if self.dirty:
            surf = pg.surfarray.make_surface(np.repeat(self.pixels[..., None], 3, axis=2).swapaxes(0,1))
            self._image.blit(pg.transform.scale(surf, self.size), (0, 0))            

            pg.draw.rect(self._image, WHITE if self.enabled else GREY * 128, (0, 0, *self.size), 1)
            self.dirty = False


        return self._image


    def draw_point(self, p: np.ndarray, value: int = 255, radius: int = 1, softness: float = .5):
        """
        Draws a soft circular brush around point p.
        - value: target intensity (0=black, 255=white)
        - radius: brush radius in pixels
        - softness: how quickly the stroke fades (larger = softer)
        """
        x, y = map(int, p)
        h, w = self.pixels.shape

        # compute affected bounding box
        xmin = max(x - radius, 0)
        xmax = min(x + radius + 1, w)
        ymin = max(y - radius, 0)
        ymax = min(y + radius + 1, h)

        # coordinate grids for the affected region
        xs = np.arange(xmin, xmax)
        ys = np.arange(ymin, ymax)
        X, Y = np.meshgrid(xs, ys)

        # distance of each pixel from brush center
        dist = np.sqrt((X - x)**2 + (Y - y)**2)

        # weight: Gaussian-like falloff
        alpha = np.exp(-(dist**2) / (2 * (softness**2)))
        alpha = np.clip(alpha, 0, 1)

        # blend into existing pixels
        region = self.pixels[ymin:ymax, xmin:xmax]
        blended = region * (1 - alpha) + value * alpha
        self.pixels[ymin:ymax, xmin:xmax] = np.clip(blended, 0, 255).astype(np.uint8)

        self.dirty = True

    def draw_line(self, a: np.ndarray, b: np.ndarray, value: int = 255, radius: int = 1, softness: float = .5):
        """Draws a continuous shaded line between a and b."""
        a = a.astype(float)
        b = b.astype(float)
        length = np.linalg.norm(a - b, np.inf)
        pts = np.linspace(a, b, int(length) + 1)
        for p in pts:
            self.draw_point(p, value, radius, softness)


    def clear(self):
        """Vymaže canvas."""
        self.pixels[:] = 0
        self.dirty = True


    def get_array(self, normalize=False):
        """Vrátí 2D numpy pole (např. pro MNIST)."""
        arr = self.pixels.copy()
        if normalize:
            arr = arr / 255.0
        return arr

    def from_array(self, arr: np.ndarray, normalize:bool=False):
        """Načte 2D pole a vykreslí jej."""
        if normalize:
            tmp = arr.copy()
            tmp -= tmp.min()
            tmp /= tmp.max()
            tmp *= 255

        self.pixels[:] = tmp.astype(np.uint8) if normalize else arr
        self.dirty = True

    def get_centered_image(self) -> np.ndarray:
        """
        Centers a grayscale image (2D array) based on its intensity centroid.
        Keeps output shape identical to input.
        """
        img = self.get_array()

        # Normalize to [0,1] for stable weighting
        img_f = img.astype(float)
        if img_f.max() > 0:
            img_f /= img_f.max()

        # Compute center of mass (y, x)
        cy, cx = center_of_mass(img_f)

        # Target center (canvas middle)
        ty, tx = np.array(img.shape) // 2

        # Shift needed to center
        shift_yx = (ty - cy, tx - cx)

        # Apply translation (use bilinear interpolation)
        centered = shift(img, shift=shift_yx, order=1, mode="constant", cval=0)

        return centered.astype(np.uint8)


    def update(self, event: pg.event.Event = None):
        super().update(event)
        m_pos = np.array(pg.mouse.get_pos())
        rel = ((m_pos - self.position) / self.cell_size).astype(int)

        # Levé tlačítko – kreslí
        match self.click(0):
            case ClickState.CLICKED:
                self.draw_point(rel)

            case ClickState.HELD:
                self.draw_line(self._last_pos, rel)


        # Pravé tlačítko – maže
        match self.click(2):
            case ClickState.CLICKED:
                self.draw_point(rel, 0)

            case ClickState.HELD:
                self.draw_line(self._last_pos, rel, 0)

        self._last_pos = rel


class BarPlot(Widget):
    def __init__(self, screen, pos, size,
                 data: np.ndarray,
                 labels=None,
                 fg=WHITE, bg=GREY * 40, border_color=GREY * 90,
                 text_color=WHITE,
                 bar_margin=2,
                 font=None,
                 tween=None,
                 color_gradient: np.ndarray = None):
        super().__init__(screen, pos, size)

        self._data = np.array(data, dtype=float)
        self._target_data = self._data.copy()
        self.labels = list(labels) if labels is not None else [f"{i}" for i in range(len(data))]

        self.bg = np.array(bg, dtype=np.uint8)
        self.border_color = np.array(border_color, dtype=np.uint8)
        self.text_color = np.array(text_color, dtype=np.uint8)
        self.bar_margin = bar_margin

        # default gradient: same color (no change)
        self.color_gradient = np.array(color_gradient if color_gradient is not None
                                       else [[152, 204, 106], [224, 47, 91]], dtype=float)

        self.font = font or pg.font.SysFont("Calibri", int(self.size[1] / len(self._data) * 0.7))
        self.tween = tween or Tween.EaseOutSine(1000, clipped=(0.0, 1.0))

        self.dirty = True

    # ------------------------------------------------------------
    # Animation property
    # ------------------------------------------------------------
    @property
    def data(self) -> np.ndarray:
        """Current display data (animated toward target)."""
        return self.tween.tweenify(self._data, self._target_data)

    def set_data(self, new_data: np.ndarray, labels=None):
        """Set new target values (and optionally labels) to animate toward."""
        new_data = np.array(new_data, dtype=float)
        if not np.allclose(new_data, self._target_data):
            self._data = self.data
            self._target_data = new_data
            self.tween.reset()

        if labels is not None:
            self.labels = list(labels)
            self.font = self.font or pg.font.SysFont("Calibri", int(self.size[1] / len(self._data) * 0.7))

    # ------------------------------------------------------------
    # Rendering
    # ------------------------------------------------------------
    @property
    def image(self):
        self._image.fill(self.bg)
        self._draw_bars()
        pg.draw.rect(self._image, self.border_color, self._image.get_rect(), 1)
        return self._image

    def _draw_bars(self):
        vals = np.clip(self.data, 0, 1) 

        n = len(vals)
        w, h = self.size
        bar_height = h / n

        c0, c1 = self.color_gradient  # shape (3,)
        for i, (val, label_text) in enumerate(zip(vals, self.labels)):
            # Compute interpolated color
            color = ((1 - val) * c0 + val * c1).astype(np.uint8)

            bar_len = int(val * (w - self.bar_margin * 2))
            y = int(i * bar_height)
            rect = pg.Rect(self.bar_margin, y + self.bar_margin,
                           bar_len, bar_height - self.bar_margin * 2)

            pg.draw.rect(self._image, color, rect)

            # Label (fixed left side)
            label_surface = self.font.render(label_text, True, self.text_color)
            text_y = int(y + bar_height / 2 - label_surface.get_height() / 2)
            text_x = 5
            self._image.blit(label_surface, (text_x, text_y + 3))