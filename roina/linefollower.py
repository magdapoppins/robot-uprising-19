from pybricks.ev3devices import ColorSensor
from pybricks.parameters import Color
from ev3dev2.motor import MoveTank


class LineFollower:
    def __init__(self, port, a, b):
        self.colorSensor = ColorSensor(port)
        self.tank_drive = MoveTank(a, b)

    def followLine():
      turnDegree = 0
      lightSensorReflectionValue self.colorSensor.reflection()
      color = self.colorSensor.color()
      # https://subscription.packtpub.com/book/hardware_and_creative/9781849519748/1/ch01lvl1sec11/proportional-line-follower-advanced
      # The base speed of the robot is controlled by a constant value
      speed = 20
      # You will need to determine a desired light sensor value for the robot to track on. You can either read the light sensor reading directly on your EV3 brick, or look at the panel on the lower-right hand corner of your screen. You should see all of the motors and sensors that are currently plugged into your brick.
      desiredValue = 49 # white value on race = 49
      # This difference is multiplied by a gain factor, which for the optical proportional line follower will probably be between 0 and 1. In this program, I chose a gain of 0.7.
      gain = 0.9

      while color != Color.RED:
        lightSensorReflectionValue = self.colorSensor.reflection()
        print('lightSensorReflectionValue', lightSensorReflectionValue)
        color = self.colorSensor.color()
        print('color', color)
        # speed - gain x (LightSensor - DesiredValue)
        motorRightPower = speed - gain * (lightSensorReflectionValue-desiredValue)
        print('motorRightPower',motorRightPower)
        # speed + gain x (LightSensor - DesiredValue)
        motorLeftPower = speed + gain * (lightSensorReflectionValue-desiredValue)
        print('motorLeftPower',motorLeftPower)

        if (color != Color.White):
          turnDegree += 1
        else:
          turnDegree = 0

        # If no white on sight for some time, change turning direction
        if turnDegree > 20:
          # speed - gain x (LightSensor - DesiredValue)
          motorRightPower = speed + gain * (lightSensorReflectionValue-desiredValue)
          print('motorRightPower',motorRightPower)
          # speed + gain x (LightSensor - DesiredValue)
          motorLeftPower = speed - gain * (lightSensorReflectionValue-desiredValue)
          print('motorLeftPower',motorLeftPower)

        self.tank_drive.on_for_seconds(SpeedPercent(motorLeftPower), SpeedPercent(motorRightPower), 0.1)