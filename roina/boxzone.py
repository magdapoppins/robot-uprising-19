from pybricks.ev3devices import ColorSensor
from pybricks.parameters import Color
from ev3dev2.motor import MoveTank
import claw

class BoxZone:
  def __init__(self, port, a, b, c):
    self.colorSensor = ColorSensor(port)
    self.tank_drive = MoveTank(a, b)
    self.grabber = claw(c)
    self.move = movement(a, b)
  
  def boxZone():
    # Go forward until finds a wall with ultrasonic sensor
    # TODO
    self.move.turnRight()
    # Go forward until finds a wall with ultrasonic sensor
    # TODO
    self.move.turnLeft()
    # turn a little left like 45 degrees or something
    self.tank_drive.on_for_seconds(SpeedPercent(-30), SpeedPercent(30), 5) # TODO: random numbers, test and change
    # Go forward until finds a wall with ultrasonic sensor
    # TODO
    # turn a little right like 45 degrees or something
    self.tank_drive.on_for_seconds(SpeedPercent(30), SpeedPercent(-30), 5) # TODO: random numbers, test and change
    # Press red button
    self.tank_drive.on_for_seconds(SpeedPercent(100), SpeedPercent(100), 5)
    # Back up a little 
    self.tank_drive.on_for_seconds(SpeedPercent(100), SpeedPercent(100), 5)
    # Grab red box
    # TODO