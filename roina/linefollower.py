from ev3dev2.sensor.lego import ColorSensor, UltrasonicSensor
from ev3dev2.motor import MoveTank, LargeMotor
import logging
import time
from roina import Claw

class LineFollower:
    def __init__(self, c_port, us_port, a, b, c):
      self.colorSensor = ColorSensor(c_port)
      self.tank_drive = MoveTank(a, b)
      self.us = UltrasonicSensor(us_port)
      self.claw = Claw(c)


    def checkWhiteLine(self):
      # reflection white on maze about 40
      # reflection grey on maze about 8
      color = self.colorSensor.color
      reflection = self.colorSensor.reflected_light_intensity
      logging.info('color: {}, reflection: {}'.format(color, reflection))
      if color == self.colorSensor.COLOR_WHITE and reflection > 30:
        return True
      else:
        return False

    def scoutForWhiteLine(self):
      # scouting for white line
      # turn left
      for i in range(10):
        self.tank_drive.on_for_seconds(30, -15, 0.1)
        if self.checkWhiteLine():
          break
      # back to original direction
      self.tank_drive.on_for_seconds(-15, 30, 0.8)
      # turn right
      for i in range(10):
        self.tank_drive.on_for_seconds(-15, 30, 0.1)
        if self.checkWhiteLine():
          break
      # back to original direction
      self.tank_drive.on_for_seconds(30, -15, 0.8)

    def followLine(self):
      # Drive forward until white line appears
      distance = self.us.value()
      logging.info('distance: {}, whiteLine {}'.format(distance, self.checkWhiteLine()))
      rounds = 0 # only for scouting purposes
      while distance > 50 and not self.checkWhiteLine():
        self.tank_drive.on(25, 25)
        if (distance < 150):
          # turn left
          self.tank_drive.on_for_seconds(60, -30, 0.65)
        
        # every now and then check for white line
        if rounds > 1000:
          if self.checkWhiteLine():
            break
          rounds = 0

        distance = self.us.value()
        rounds += 1

      color = self.colorSensor.color
      self.tank_drive.on(15, 15)
      while color != self.colorSensor.COLOR_RED:
        color = self.colorSensor.color
        if color == self.colorSensor.COLOR_WHITE:
          # turn right
          self.tank_drive.on(-40, 60)
        elif color == self.colorSensor.COLOR_YELLOW:
          # go a little forward, then back and turn left
          self.tank_drive.on_for_seconds(60, 60, 0.5)
          self.claw.down()
          self.claw.down()
          self.claw.down()
          self.claw.up()
          self.claw.up()
          self.claw.up()
          self.tank_drive.on_for_seconds(-60, -60, 1.5)
          self.tank_drive.on_for_seconds(60, -60, 0.7)
          time.sleep(5)
        else:
          # turn left
          self.tank_drive.on(60, -30)
      
      if color == self.colorSensor.COLOR_RED: # go to next section
        # go to next section: drive forward until red color ends
        color = self.colorSensor.color
        while color == self.colorSensor.COLOR_RED:
          self.tank_drive.on(50, 50)
          color = self.colorSensor.color
