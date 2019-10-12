from ev3dev2.motor import MediumMotor


class Claw:
    def __init__(self, output):
        self.claw = MediumMotor(output)

    def up(self):
        self.claw.on_for_degrees(30, 360)

    def down(self):
        self.claw.on_for_degrees(30, -360)
