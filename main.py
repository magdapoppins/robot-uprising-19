#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank

# Outputs = Port.A, Port.B.... etc
# Inputs = Port.S1, Port.S2... etc
#  DOcs https://le-www-live-s.legocdn.com/sc/media/files/ev3-micropython/ev3micropythonv100-71d3f28c59a1e766e92a59ff8500818e.pdf

# Write your program here

tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)

# drive in a turn for 5 rotations of the outer motor
# the first two parameters can be unit classes or percentages.

# drive in a different turn for 3 seconds

brick.sound.beep()
areas = ["FOLLOW_LINE", "PRESS_BTN", "FOREST"]

wheel_diameter = 56
axle_track = 114

area = areas[0]

c_sensor = ColorSensor(Port.S2)
last_ambient = 2000


while True:
    c = c_sensor.color()
    if c == Color.RED:
        area = areas[areas.index[area] + 1]
        tank_drive.on_for_seconds(SpeedPercent(-30), SpeedPercent(30), 0.1)

    if area == areas[0]:
        c = c_sensor.color()
        a = c_sensor.ambient()
        print(a, c == Color.WHITE)
        if c == Color.WHITE and a > 1:
            if a < last_ambient:
                tank_drive.on_for_seconds(
                    SpeedPercent(100), SpeedPercent(75), 0.1)
        else:
            tank_drive.on_for_seconds(SpeedPercent(-20), SpeedPercent(20), 0.1)
        last_ambient = a
    elif area == areas[1]:
        print("asd")
    elif area == areas[2]:
        print("asd")
        
