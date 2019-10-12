from ev3dev2.sensor.lego import ColorSensor, UltrasonicSensor
from ev3dev2.motor import MoveTank, LargeMotor, OUTPUT_A, OUTPUT_B
import logging

class LineFollower:
    def __init__(self, c_port, us_port, a, b):
      self.colorSensor = ColorSensor(c_port)
      self.tank_drive = MoveTank(a, b)
      self.us = UltrasonicSensor(us_port)

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

    def followLine(self):
      # Drive forward until white line appears
      distance = self.us.value()
      logging.info('distance: {}, whiteLine {}'.format(distance, self.checkWhiteLine()))
      wallFound = False
      while distance > 50 and not self.checkWhiteLine():
        self.tank_drive.on(25, 25)
        if wallFound:
          # scouting for white line
          # turn left
          for i in range(10):
            self.tank_drive.on_for_seconds(30, -15, 0.1)
            if self.checkWhiteLine():
              break
          # back to original direction
          self.tank_drive.on_for_seconds(-15, 30, 0.3)
          # turn right
          for i in range(5):
            self.tank_drive.on_for_seconds(-15, 30, 0.1)
            if self.checkWhiteLine():
              break
          # back to original direction
          self.tank_drive.on_for_seconds(30, -15, 0.2)
          # DRIVE
          self.tank_drive.on_for_seconds(15, 15, 1)

        if (distance < 100):
          # turn left
          wallFound = True
          for i in range(10):
            self.tank_drive.on_for_seconds(30, -15, 0.2)
            if self.checkWhiteLine():
              break

        distance = self.us.value()

      color = self.colorSensor.color
      self.tank_drive.on(15, 15)
      while color != self.colorSensor.COLOR_RED:
        color = self.colorSensor.color
        if color != self.colorSensor.COLOR_BLACK:
          # turn left
          self.tank_drive.on(60, -30)
        else:
          # turn right
          self.tank_drive.on(-30, 60)

