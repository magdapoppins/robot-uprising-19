#!/usr/bin/env python3

from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C
from roina import Claw, Movement, Controller
import sys
import logging

# Outputs = Port.A, Port.B.... etc
# Inputs = Port.S1, Port.S2... etc
# DOcs https://le-www-live-s.legocdn.com/sc/media/files/ev3-micropython/ev3micropythonv100-71d3f28c59a1e766e92a59ff8500818e.pdf

# Write your program here

move = Movement(OUTPUT_A, OUTPUT_B)

grabber = Claw(OUTPUT_C)

# follower = linefollower(Port.S2, OUTPUT_A, OUTPUT_B)

move.move()

grabber.up()
grabber.down()

controller = Controller()
