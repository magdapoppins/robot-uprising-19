import evdev
from threading import Thread
import logging


class Controller(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
        self.gamepad = evdev.InputDevice(self.devices[0].fn)
        self.start()

    def run(self):
        for event in self.gamepad.read_loop():
            logging.info('controller input:')
            logging.info('type: {}'.format(event.type))
            logging.info('code: {}'.format(event.code))
            logging.info('---')
