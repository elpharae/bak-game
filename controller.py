import pygame
import model
from eventmanager import *

class Keyboard(object):
    
    def __init__(self, event_mng, model):
        self.event_mng = event_mng
        event_mng.register_listener(self)
        self.model = model
    
    def notify(self, event):
        if isinstance(event, TickEvent):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.event_mng.post(QuitEvent())
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.event_mng.post(QuitEvent())
                    else:
                        self.event_mng.post(InputEvent(event.unicode, None))