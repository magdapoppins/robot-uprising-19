from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.motor import MoveTank, LargeMotor, OUTPUT_A, OUTPUT_B
import logging

class LineFollower:
    def __init__(self, c_port, a, b):
      self.colorSensor = ColorSensor(c_port)
      self.tank_drive = MoveTank(a, b)
      self.motor_right = LargeMotor(OUTPUT_A)
      self.motor_left = LargeMotor(OUTPUT_B)

    def followLine(self):
      color = self.colorSensor.color
      # https://subscription.packtpub.com/book/hardware_and_creative/9781849519748/1/ch01lvl1sec11/proportional-line-follower-advanced
      # The base speed of the robot is controlled by a constant value
      speed = 15
      # You will need to determine a desired light sensor value for the robot to track on. You can either read the light sensor reading directly on your EV3 brick, or look at the panel on the lower-right hand corner of your screen. You should see all of the motors and sensors that are currently plugged into your brick.
      desiredValue = 65 # white value on race = 49, testing viiva 65 ja lattia 8 eli keskiarvo 26
      # This difference is multiplied by a gain factor, which for the optical proportional line follower will probably be between 0 and 1.
      gain = 0.8

      self.tank_drive.on(20, 20)
      while color != self.colorSensor.COLOR_RED:
        color = self.colorSensor.color
        if color != self.colorSensor.COLOR_WHITE:
          self.tank_drive.stop()
          # check your left
          reflectionOnLeft = 0
          for i in range(5):
            self.tank_drive.on_for_seconds(20, -20, 0.1)
            reflectionOnLeft += self.colorSensor.reflected_light_intensity
          self.tank_drive.on_for_seconds(-20, 20, 0.3)
          # check your right
          reflectionOnRight = 0
          for i in range(5):
            self.tank_drive.on_for_seconds(-20, 20, 0.1)
            reflectionOnRight += self.colorSensor.reflected_light_intensity
          # move
          logging.info("reflectionOnLeft", reflectionOnLeft, "reflectionOnRight", reflectionOnRight)
          if reflectionOnLeft > reflectionOnRight:
            self.tank_drive.on_for_seconds(20, -20, 0.7)
          if reflectionOnRight > reflectionOnLeft:
            self.tank_drive.on_for_seconds(-20, 20, 0.3)
          self.tank_drive.on(20, 20)

        # lightSensorReflectionValue = self.colorSensor.reflected_light_intensity
        # logging.info('lightSensorReflectionValue', lightSensorReflectionValue)
        # color = self.colorSensor.color
        # logging.info('color', color)
        # # speed - gain x (LightSensor - DesiredValue)
        # motorRightPower = speed - gain * (lightSensorReflectionValue-desiredValue)
        # logging.info('motorRightPower',motorRightPower)
        # # speed + gain x (LightSensor - DesiredValue)
        # motorLeftPower = speed + gain * (lightSensorReflectionValue-desiredValue)
        # logging.info('motorLeftPower',motorLeftPower)
        #self.motor_right.on_for_rotations(motorRightPower, 0.1)
        #self.motor_left.on_for_rotations(motorLeftPower, 0.1)
        #self.tank_drive.on_for_seconds(motorRightPower, motorLeftPower, 0.1)