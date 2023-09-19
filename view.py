import pygame
from model import Game
from eventmanager import *
from settings import *

class View(object):
    
    def __init__(self, event_mng: EventManager, model: Game):
        self.event_mng = event_mng
        event_mng.register_listener(self)
        self.screen = None
        self.clock = None
        self.smallfont = None
        self.is_initialized = False

    def notify(self, event: Event):
        
        if isinstance(event, InitializeEvent):
            self.initialize()
        elif isinstance(event, QuitEvent):
            self.is_initialized = False
            pygame.quit()
        elif isinstance(event, TickEvent):
            self.renderall()
            self.clock.tick(FPS)

    def renderall(self):
        if not self.is_initialized:
            return

        pygame.display.flip()

    def initialize(self):
        result = pygame.init()
        pygame.font.init()
        pygame.display.set_caption(TITLE)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.smallfont = pygame.font.Font(None, 40)
        self.is_initialized = True