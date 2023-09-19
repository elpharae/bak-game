
class Event(object):
    def __init__(self) -> None:
        self.name = "Generic Event"
    def __str__(self):
        return self.name

class QuitEvent(Event):
    def __init__(self):
        self.name = "Quit Event"
    
class TickEvent(Event):
    def __init__(self):
        self.name = "Tick Event"

class InputEvent(Event):
    def __init__(self, unicode_char, click_pos) -> None:
        self.name = "Input Event"
        self.char = unicode_char
        self.click_pos = click_pos
    def __str__(self):
        return '%s %s %s' % (self.name, self.char, self.click_pos)

class InitializeEvent(Event):
    def __init__(self):
        self.name = "Initialize Event"
    
class EventManager(object):
    def __init__(self):
        from weakref import WeakKeyDictionary
        self.listeners = WeakKeyDictionary()

    def register_listener(self, listener):
        self.listeners[listener] = 1
    
    def unregister_listener(self, listener):
        if listener in self.listeners.keys():
            del self.listeners[listener]
    
    def post(self, event):
        if not isinstance(event, TickEvent):
            print(str(event))
        
        for listener in self.listeners.keys():
            listener.notify(event)
        