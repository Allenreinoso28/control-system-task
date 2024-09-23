import pygame

class Controller:
    def __init__(self):
        pygame.init()
        pygame.joystick.init()
        if pygame.joystick.get_count() == 0:
            print("CONTROLLER NOT FOUND")
            pygame.quit
            quit()
        self.controller = pygame.joystick.Joystick(0)
        self.controller.init()
        print("CONTROLLER HAS BEEN CONNECTED")

    def get_axis(self, axis_mapping):
        return self.controller.get_axis(axis_mapping)

    def get_button(self, button_mapping):
        return self.controller.get_button(button_mapping)