from ev3dev2.sensor.lego import (TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)

from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, SpeedPercent, SpeedRPM, MoveTank

# Outputs = Port.A, Port.B.... etc
# Inputs = Port.S1, Port.S2... etc
#  DOcs https://le-www-live-s.legocdn.com/sc/media/files/ev3-micropython/ev3micropythonv100-71d3f28c59a1e766e92a59ff8500818e.pdf

# Write your program here
class Movement:

    def __init__(self, motor1, motor2, us_port, c_port):
        self.tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)
        self.us = UltrasonicSensor(us_port)
        self.colorSensor = ColorSensor(c_port)

    def turnLeft():
        # Turn 90 degrees left
        # TODO: random numbers, test and change
        self.tank_drive.on_for_seconds(SpeedPercent(-50), SpeedPercent(50), 5)

    def turnRight():
        # Turn 90 degrees right
        # TODO: random numbers, test and change
        self.tank_drive.on_for_seconds(SpeedPercent(50), SpeedPercent(-50), 5)

    def driveUntilColorAppears(colorToFind):
        # Drive forward until white line appears
        color = self.colorSensor.color()
        while color != colorToFind:
            color = self.colorSensor.color()
            self.tank_drive.on_for_seconds(
                SpeedPercent(100), SpeedPercent(100), 0.2)

    def driveUntilColorEnds(colorToFollow):
      # Drive forward until white line appears
      color = self.colorSensor.color()
      while color == colorToFollow:
        color = self.colorSensor.color()
        self.tank_drive.on_for_seconds(SpeedPercent(100), SpeedPercent(100), 0.2)

    def driveUntilWallAhead():
        distance = self.us.value()
        print(str(distance) + " " + mm)
        while distance > 30:
            distance = self.us.value()
            self.tank_drive.on_for_seconds(
                SpeedPercent(100), SpeedPercent(100), 0.2)

    def move_line(self):
        tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)

        # drive in a turn for 5 rotations of the outer motor
        # the first two parameters can be unit classes or percentages.

        # drive in a different turn for 3 seconds

        brick.sound.beep()
        areas = ["PARKING", "SPINNERS", "FOREST",
                 "BOXZONE", "PRESS_BTN", "MAZE"]
        area = areas.pop()

        wheel_diameter = 56
        axle_track = 114

        c_sensor = ColorSensor(Port.S2)
        last_ambient = 2000

        while True:
            c = c_sensor.color()
            if c == Color.RED:
                if area == "MAZE":
                    area = areas.pop()
                    print(area)
                tank_drive.on_for_seconds(
                    SpeedPercent(-30), SpeedPercent(30), 0.1)

            if area == "MAZE":
                c = c_sensor.color()
                a = c_sensor.ambient()
                #print(a, c == Color.WHITE)
                if c == Color.WHITE and a > 1:
                    if a < last_ambient:
                        tank_drive.on_for_seconds(
                            SpeedPercent(100), SpeedPercent(75), 0.1)
                else:
                    tank_drive.on_for_seconds(
                        SpeedPercent(-20), SpeedPercent(20), 0.1)
                last_ambient = a
