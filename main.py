#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# Outputs = Port.A, Port.B.... etc
# Inputs = Port.S1, Port.S2... etc
#  DOcs https://le-www-live-s.legocdn.com/sc/media/files/ev3-micropython/ev3micropythonv100-71d3f28c59a1e766e92a59ff8500818e.pdf

# Write your program here
SPEED = 1000000
brick.sound.beep()
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

wheel_diameter = 56
axle_track = 114

robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)
c_sensor = ColorSensor(Port.S1)
last_ambient = 2000
while True:
    c = c_sensor.color()
    a = c_sensor.ambient()
    print(a,c == Color.WHITE)
    if c == Color.WHITE and a > 1:
        if a < last_ambient:
            robot.drive(SPEED, 666)
        robot.drive(SPEED,0)
        last_ambient = a
    else:
        robot.stop()