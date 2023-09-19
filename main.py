import model
import view
import controller
import eventmanager

def run():
    event_mng = eventmanager.EventManager()
    game_model = model.Game(event_mng)
    keyboard = controller.Keyboard(event_mng, game_model)
    graphics = view.View(event_mng, game_model)
    game_model.run()

if __name__ == '__main__':
    run()