from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.motor import MoveTank, LargeMotor, OUTPUT_A, OUTPUT_B
import logging

class LineFollower:
    def __init__(self, c_port, a, b):
      self.colorSensor = ColorSensor(c_port)
      self.tank_drive = MoveTank(a, b)

    def followLine(self):
      # Drive forward until white line appears
      color = self.colorSensor.color
      while color != self.colorSensor.COLOR_WHITE:
          color = self.colorSensor.color
          self.tank_drive.on_for_seconds(15, 15, 3)
          # turn right
          self.tank_drive.on_for_seconds(60, -30, 0.5)
          color = self.colorSensor.color
          if color == self.colorSensor.COLOR_WHITE: 
            break
          # turn left
          for i in range(5):
            self.tank_drive.on_for_seconds(-30, 60, 0.1)
            color = self.colorSensor.color
            if color == self.colorSensor.COLOR_WHITE: 
              break
          # turn right
          self.tank_drive.on_for_seconds(60, -30, 0.5)
          color = self.colorSensor.color
          if color == self.colorSensor.COLOR_WHITE: 
            break

      color = self.colorSensor.color
      self.tank_drive.on(15, 15)
      while color != self.colorSensor.COLOR_RED:
        color = self.colorSensor.color
        if color != self.colorSensor.COLOR_BLACK:
          # turn right
          self.tank_drive.on(60, -30)
        else:
          # turn left
          self.tank_drive.on(-30, 60)

