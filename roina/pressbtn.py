from ev3dev2.sensor.lego import ColorSensor, UltrasonicSensor
from ev3dev2.motor import MoveTank
from roina import Claw
from roina import Movement

class PressButton:
  def __init__(self, c_port, a, b, c):
    self.colorSensor = ColorSensor(port)
    self.tank_drive = MoveTank(a, b)
    self.move = Movement(a, b, us_port, c_port)

  # 1. Press red button on the corner
  # 2. Press the yellow button
  # 3. Go to the next section
  def pressButton():
      self.move.driveUntilColorAppears(Color.White)
      self.move.turnRight()
      # Boop red button with butt
      self.tank_drive.on_for_seconds(SpeedPercent(-50), SpeedPercent(-50), 5)
      self.move.driveUntilColorAppears(Color.Red) # middle part red
      self.move.turnRight()
      self.move.driveUntilWallAhead()
      self.tank_drive.on_for_seconds(SpeedPercent(-50), SpeedPercent(-50), 1)
      self.move.turnLeft()
      self.move.driveUntilWallAhead()
      # Hope that yellow button gets pushed
      self.move.turnLeft()
      self.move.driveUntilWallAhead()
      self.move.turnRight()
      self.move.driveUntilColorAppears(Color.Red) # section change