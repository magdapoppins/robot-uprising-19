from pybricks.ev3devices import ColorSensor
from pybricks.parameters import Color
from ev3dev2.motor import MoveTank
import claw
import movement

class PressButton:
  def __init__(self, port, a, b, c):
    self.colorSensor = ColorSensor(port)
    self.tank_drive = MoveTank(a, b)
    self.grabber = claw(c)
    self.move = movement(a, b)

  def driveUntilColorAppears(colorToFind):
      # Drive forward until white line appears
      color = self.colorSensor.color()
      while color != colorToFind:
        color = self.colorSensor.color()
        self.tank_drive.on_for_seconds(SpeedPercent(100), SpeedPercent(100), 0.2)

  # 1. Press red button on the corner
  # 2. Go up the ramp
  # 3. Go to the hole and drop the USB stick there
  # 4. Go back down
  # BONUS: Press yellow button
  # 5. Täysii forward to the next section
  def pressButton():
      # Drive forward until white line appears
      color = self.colorSensor.color()
      while color != Color.White:
        color = self.colorSensor.color()
        self.tank_drive.on_for_seconds(SpeedPercent(100), SpeedPercent(100), 0.2)
      self.move.turnRight()
      # Boop red button with butt
      self.tank_drive.on_for_seconds(SpeedPercent(-50), SpeedPercent(-50), 5)
      # Go a little forward
      self.tank_drive.on_for_seconds(SpeedPercent(100), SpeedPercent(100), 5)
      self.move.turnRight()
      driveUntilColorAppears(Color.White)
      # ( TODO: and adjust direction with the line? )
      self.move.turnLeft()
      # Drive forward TÄYSII until grey floor ends, also allow white line
      color = self.colorSensor.color()
      reflection = self.colorSensor.reflection()
      gray = 30 # TODO: check gray reflection value 
      while (gray-5 < reflection < gray+5) or color == Color.White:
        color = self.colorSensor.color()
        self.tank_drive.on_for_seconds(SpeedPercent(100), SpeedPercent(100), 0.2)
      # Turn left and go forward until black shiny line appears
      self.move.turnLeft()
      color = self.colorSensor.color()
      while color != Color.Black:
        color = self.colorSensor.color()
        self.tank_drive.on_for_seconds(SpeedPercent(100), SpeedPercent(100), 0.2)
      # Go backwards a little, turn right and go forward until white line appears
      self.tank_drive.on_for_seconds(SpeedPercent(-50), SpeedPercent(-50), 2)
      self.move.turnRight()
      driveUntilColorAppears(Color.White)
      # Drop usb stick
      self.grabber.down()
      # GO BACK
      # Go back a little
      self.tank_drive.on_for_seconds(SpeedPercent(-50), SpeedPercent(-50), 2)
      self.move.turnRight()
      driveUntilColorAppears(Color.White)
      self.tank_drive.on_for_seconds(SpeedPercent(50), SpeedPercent(50), 2)
      self.move.turnRight()
      # Go forward until nose BOOP
      # TODO
      self.move.turnRight()
      # Go forward until nose BOOP
      # TODO
      self.move.turnRight()
      driveUntilColorAppears(Color.Yellow)
      self.move.turnLeft()
      # Push button
      self.tank_drive.on_for_seconds(SpeedPercent(50), SpeedPercent(50), 5)
      self.move.turnRight()
      # TÄYSII to the next section
      driveUntilColorAppears(Color.Red) # middle part red
      driveUntilColorAppears(Color.Red) # section change