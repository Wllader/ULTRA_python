import pygame as pg, numpy as np

#Todo Vytvořit základní PongEntity
#Todo odvodit od ní PongPlayer, PongBot a PongBall objekty
#Todo implementovat základní chování objektů


class PongEntity(pg.sprite.Sprite): pass

class PongPlayer(PongEntity): pass

class PongBot(PongEntity): pass

class PongBall(PongEntity): pass