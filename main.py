#!/usr/bin/env python3

from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C
from roina import Claw, Movement, Controller, Linefollower, BoxZone
import sys
import logging

# Outputs = Port.A, Port.B.... etc
# Inputs = Port.S1, Port.S2... etc
# DOcs https://le-www-live-s.legocdn.com/sc/media/files/ev3-micropython/ev3micropythonv100-71d3f28c59a1e766e92a59ff8500818e.pdf

# Write your program here
brick.sound.beep()
theEnd = false
while not theEnd:
  move = Movement(OUTPUT_A, OUTPUT_B, Port.S3, Port.S2)
  # pre-stuff: close claws for usb stick
  grabber = Claw(OUTPUT_C)
  grabber.down()

  # first section MAZE
  follower = Linefollower(Port.S2, Port.S3, OUTPUT_A, OUTPUT_B) 
  follower.followLine()

  # go to next section
  move.driveUntilColorEnds(Color.RED)

  # second section PRESS_BTN
  pressButton = pressbtn(Port.S2, Port.S3, OUTPUT_A, OUTPUT_B, OUTPUT_C)
  pressButton.pressButton()

  # go to next section
  move.driveUntilColorEnds(Color.RED)

  # third section BOXZONE
  boxzone = BoxZone(Port.S2, OUTPUT_A, OUTPUT_B, OUTPUT_C)
