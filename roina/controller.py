import evdev
from threading import Thread
import logging

CONTROL_MAPPING = {
    'L1': 310,
    'R1': 311,
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
        self.speed = 0
        self.x_axis = 0

    def stop(self):
        self.movement.stop()
        self.stopped = True

    def start(self):
        self.movement.stop()
        self.stopped = True

    def run(self):
        print(self.side, "wheel is ready")
        while self.work:
            if not self.stopped:
                left = speed + (x_axis * self.speed)
                right = speed - (x_axis * self.speed)
                self.movement.free_move(left, right)

        self.movement.stop()


class Controller(Thread):
    def __init__(self, movement, main_thread):
        Thread.__init__(self)
        self.daemon = True
        self.devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
        self.gamepad = evdev.InputDevice(self.devices[0].fn)

        self.buttons = {
            304: self.cross_fn,
            308: None,
            307: None,
            305: None,
            310: None,
            311: None,
        }

        self.main_thread = main_thread

        self.moving = True
        self.movement_thread = MovementThread(movement)

    def cross_fn(self):
        if self.moving:
            self.moving = False
            self.movement_thread.stop()
            self.main_thread.start()
        else:
            self.main_thread.stop()
            self.movement_thread.start()
            self.movement = True

    def listen(self):
        self.start()

    def run(self):
        for event in self.gamepad.read_loop():

            if event.type == 1:
                logging.info(event.code)
                code_fn = buttons.get(event.code, None)
                if code_fn:
                    code_fn()

            elif event.type == 3 and self.moving:
                if event.code == 5:  # right stick Y
                    logging.info(event.value)
                    val = float(event.value) / 255 * 200 - 100
                    self.movement.free_move(val)

                if event.code == 0:  # left stick X
                    logging.info(event.value)
                    if event.value > 133:
                        self.movement_thread.x_axis = 1
                    elif event.value < 122:
                        self.movement_thread.x_axis = -1
                    else:
                        self.movement_thread.x_axis = 0
