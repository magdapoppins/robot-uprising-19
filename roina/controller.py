import evdev
from threading import Thread
import logging

CONTROL_MAPPING = {
    'L1': 310,
    'R1': 311,
    'CROSS': 304,
    'SQUARE': 308,
    'TRIANGLE': 307,
    'CIRCLE': 305,
}


class MovementThread(Thread):
    def __init__(self, movement):
        Thread.__init__(self)
        self.daemon = True
        self.stopped = False
        self.movement = movement
        self.left_speed = 0
        self.right_speed = 0

    def stop(self):
        self.movement.stop()

    def run(self):
        print(self.side, "wheel is ready")
        while self.work:
            self.motor.on(duty_cycle_sp=self.speed)

        self.movement.stop()


class Controller(Thread):
    def __init__(self, movement):
        Thread.__init__(self)
        self.daemon = True
        self.devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
        self.gamepad = evdev.InputDevice(self.devices[0].fn)
        self.buttons = {
            304: None,
            308: None,
            307: None,
            305: None,
            310: None,
            311: None,
        }
        self.movement_thread = MovementThread(movement)

    def set_button(self):
        self.start()

    def run(self):
        self.start()

    def run(self):
        for event in self.gamepad.read_loop():
            if event.type == 3:
                if event.code == 5:  # right stick Y
                    self.movement.free_move(left_speed, right_speed)

                if event.code == 0:  # left stick X
                    if event.value > 133:
                        r_motor_thread.pause = True
                    elif event.value < 122:
                        l_motor_thread.pause = True
                    else:
                        l_motor_thread.pause = False
                        r_motor_thread.pause = False
            elif event.type == 1:

            logging.info('controller input:')
            logging.info('type: {}'.format(event.type))
            logging.info('code: {}'.format(event.code))
            logging.info('---')
