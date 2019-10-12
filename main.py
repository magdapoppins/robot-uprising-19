#!/usr/bin/env python3

from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C
<<<<<<< HEAD
from roina import Claw, Movement, Controller, Linefollower
import sys
import logging
=======
from pybricks.parameters import (Port)
from roina import claw, movement, linefollower, pressbtn, boxzone
>>>>>>> Add sections to main

# Outputs = Port.A, Port.B.... etc
# Inputs = Port.S1, Port.S2... etc
# DOcs https://le-www-live-s.legocdn.com/sc/media/files/ev3-micropython/ev3micropythonv100-71d3f28c59a1e766e92a59ff8500818e.pdf

# Write your program here
brick.sound.beep()
theEnd = false
while not theEnd:
  move = movement(OUTPUT_A, OUTPUT_B, Port.S3, Port.S2)
  # pre-stuff: close claws for usb stick
  grabber = claw(OUTPUT_C)
  grabber.down()

  # first section MAZE
  follower = linefollower(Port.S2, Port.S3, OUTPUT_A, OUTPUT_B) 
  follower.followLine()

  # go to next section
  move.driveUntilColorEnds(Color.RED)

  # second section PRESS_BTN
  pressButton = pressbtn(Port.S2, Port.S3, OUTPUT_A, OUTPUT_B, OUTPUT_C)
  pressButton.pressButton()

  # go to next section
  move.driveUntilColorEnds(Color.RED)

  # third section BOXZONE
  boxZone = boxzone(Port.S2, OUTPUT_A, OUTPUT_B, OUTPUT_C)

# move = movement(OUTPUT_A, OUTPUT_B, Port.S3, Port.S2)

# grabber = claw(OUTPUT_C)

# follower = linefollower(Port.S2, Port.S3, OUTPUT_A, OUTPUT_B, OUTPUT_C) 

# move.move()

# grabber.up()
# grabber.down()

# follower.followLine()
