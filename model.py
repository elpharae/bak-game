import pygame
from eventmanager import *

class Game(object):
    
    def __init__(self, event_mng) -> None:
        self.event_mng = event_mng   
        event_mng.register_listener(self)
        self.running = True

    def notify(self, event):
        if isinstance(event, QuitEvent):
            self.running = False
    
    def run(self):
        self.running = True
        self.event_mng.post(InitializeEvent())
        while self.running:
            tick = TickEvent()
            self.event_mng.post(tick)
    
