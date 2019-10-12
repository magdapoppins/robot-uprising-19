from ev3dev2.sound import Sound
from ev3dev2.led import Leds


class BM:
    # ROBOTS HAVE FEELINGS TOO
    # BM = Big eMotions
    def __init__(self):
        self.light = Leds()
        self.sound = Sound()

    # A JOLLY GOOD TIME
    def calm(self):
        self.sound(100, "Sounds/Cat purr")
        self.light(Color.GREEN)

    # YOUR MOTHER WAS A HAMSTER
    def aggro(self):
        self.sound(100, "Sounds/Overpower")
        self.light(Color.RED)

    # AND YOUR FATHER SMELLS LIKE ELDERBERRIES
    def beep(self):
        self.sound.beep()

    # HIDE, THE KNIGHTS WHO SAY 'NI' ARE NEAR!
    def stealth(self):
        self.sound(100, "Sounds/Boo")
        self.light(None)

    # SNAKE? SNAKE??? SNAAKEEEEEEEE????
    def scared(self):
        self.sound(100, "Sounds/Uh-oh")
        self.light(Color.YELLOW)
