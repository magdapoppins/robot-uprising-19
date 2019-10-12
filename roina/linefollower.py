from ev3dev2.sensor.lego import ColorSensor, UltrasonicSensor
from ev3dev2.motor import MoveTank, LargeMotor, OUTPUT_A, OUTPUT_B
import logging

class LineFollower:
    def __init__(self, c_port, us_port, a, b):
      self.colorSensor = ColorSensor(c_port)
      self.tank_drive = MoveTank(a, b)
      self.us = UltrasonicSensor(us_port)

    def followLine(self):
      # Drive forward until white line appears
      color = self.colorSensor.color
      distance = self.us.value()
      logging.info('distance: {}, color {}'.format(distance, color))
      wallFound = False
      while distance > 50 and color != self.colorSensor.COLOR_WHITE:
        self.tank_drive.on(25, 25)
        if wallFound:
          # scouting for white line
          # turn left
          for i in range(10):
            self.tank_drive.on_for_seconds(30, -15, 0.1)
            color = self.colorSensor.color
            if color == self.colorSensor.COLOR_WHITE:
              break
          # back to original direction
          self.tank_drive.on_for_seconds(-15, 30, 0.4)
          # turn right
          for i in range(5):
            self.tank_drive.on_for_seconds(-15, 30, 0.1)
            color = self.colorSensor.color
            if color == self.colorSensor.COLOR_WHITE:
              break
          # back to original direction
          self.tank_drive.on_for_seconds(30, -15, 0.2)
          # DRIVE
          self.tank_drive.on_for_seconds(15, 15, 0.5)

        if (distance < 100):
          # turn left
          wallFound = True
          for i in range(10):
            self.tank_drive.on_for_seconds(30, -15, 0.2)
            color = self.colorSensor.color
            if color == self.colorSensor.COLOR_WHITE:
              break

        color = self.colorSensor.color
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

