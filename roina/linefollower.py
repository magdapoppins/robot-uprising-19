from pybricks.ev3devices import ColorSensor

class LineFollower:
    def __init__(self, port, a, b):
        self.colorSensor = ColorSensor(port)
        self.tank_drive = MoveTank(a, b)

    def followLine():
      # TODO: tank always turns left if no white line found, so turning right is hard or even impossible 🙀

      # https://subscription.packtpub.com/book/hardware_and_creative/9781849519748/1/ch01lvl1sec11/proportional-line-follower-advanced
      # The base speed of the robot is controlled by a constant value
      speed = 20
      # You will need to determine a desired light sensor value for the robot to track on. You can either read the light sensor reading directly on your EV3 brick, or look at the panel on the lower-right hand corner of your screen. You should see all of the motors and sensors that are currently plugged into your brick.
      desiredValue = 49 # white value on race = 49
      lightSensorReflectionValue = self.colorSensor.reflection()
      print('lightSensorReflectionValue', lightSensorReflectionValue)
      # This difference is multiplied by a gain factor, which for the optical proportional line follower will probably be between 0 and 1. In this program, I chose a gain of 0.7.
      gain = 0.9
      # speed - gain x (LightSensor - DesiredValue)
      motorRightPower = speed - gain * (lightSensorReflectionValue-desiredValue)
      print('motorRightPower',motorRightPower)
      # speed + gain x (LightSensor - DesiredValue)
      motorLeftPower = speed + gain * (lightSensorReflectionValue-desiredValue)
      print('motorLeftPower',motorLeftPower)
      self.tank_drive.on_for_seconds(SpeedPercent(motorLeftPower), SpeedPercent(motorRightPower), 0.1)