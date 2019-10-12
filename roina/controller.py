import evdev


class Controller:
    def __init__(self):
        self.devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
        self.gamepad = evdev.InputDevice(self.devices[0].fn)

        for event in self.gamepad.read_loop():
            print(event.type)
            print(event.code)
            print('---')
