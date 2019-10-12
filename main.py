#!/usr/bin/env pybricks-micropython

from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C
from pybricks.parameters import (Port)
from roina import claw, movement, linefollower

# Outputs = Port.A, Port.B.... etc
# Inputs = Port.S1, Port.S2... etc
#  DOcs https://le-www-live-s.legocdn.com/sc/media/files/ev3-micropython/ev3micropythonv100-71d3f28c59a1e766e92a59ff8500818e.pdf

# Write your program here

move = movement(OUTPUT_A, OUTPUT_B, Port.S3, Port.S2)

grabber = claw(OUTPUT_C)

follower = linefollower(Port.S2, Port.S3, OUTPUT_A, OUTPUT_B, OUTPUT_C) 

move.move()

grabber.up()
grabber.down()

follower.followLine()
