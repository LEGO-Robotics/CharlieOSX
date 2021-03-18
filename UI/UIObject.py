from profileHelper import ProfileHelper
from pybricks.parameters import Button, Color
from pybricks.media.ev3dev import Image, ImageFile, Font, SoundFile

# from UI.tools import Box


class UIObject:
    def __init__(self, name: str, brick: EV3Brick, bounds: Box, contentType, content, padding=(0, 0, False), font=Font(family='arial', size=11), visible=True):
        # self.logger = logger
        self.name = name
        self.brick = brick
        self.bounds = bounds
        self.padding = padding
        self.contentType = contentType
        self.content = content
        self.font = font
        self.visibility = visible
        self.radius = 0
        self.selected = False

    def getName(self):
        return self.name

    def setVisibility(self, visibility: bool):
        self.visibility = visibility

    def getVisibility(self):
        return self.visibility

    def update(self):
        pass

    def draw(self, selected=False):
        if self.padding[2]:
            x = self.padding[0]
            y = self.padding[1]
        else:
            x = self.bounds.x + self.padding[0]
            y = self.bounds.y + self.padding[1]
        if self.visibility:
            if self.contentType == 'img':
                if self.selected:
                    self.radius = 5
                else:
                    self.radius = 0
                self.brick.screen.draw_image(x, y, self.content, transparent=Color.RED)
            elif self.contentType == 'textBox':
                self.brick.screen.set_font(self.font)
                self.brick.screen.draw_box(x, y, x + self.bounds.width, y + self.bounds.height, r=2, fill=True, color=Color.WHITE)
                self.brick.screen.draw_box(x, y, x + self.bounds.width, y + self.bounds.height, r=2, fill=False if not selected else True, color=Color.BLACK)
                self.brick.screen.draw_text(self.bounds.x + 1, self.bounds.y + 1, self.content, text_color=Color.BLACK if not selected else Color.WHITE)
        else:
            if self.contentType == 'textBox':
                self.brick.screen.draw_box(x, y, x + self.bounds.width, y + self.bounds.height, r=2, fill=True, color=Color.WHITE)

    def setClickAction(self, action: Function):
        self.clickAction = action

    def click(self):
        self.clickAction()
