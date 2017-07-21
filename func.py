from __future__ import print_function
from __future__ import division
from builtins import input
##The above lines are random crap
import time

from BrickPi import *


BrickPiSetup()

##BrickPi.MotorEnable[PORT_A] = 1
##BrickPi.MotorEnable[PORT_B] = 1
##BrickPi.MotorEnable[PORT_C] = 1
##BrickPi.MotorEnable[PORT_D] = 1
##BrickPi.SensorType[PORT_1] = TYPE_SENSOR_TOUCH
##BrickPi.SensorType[PORT_2] = TYPE_SENSOR_TOUCH
##BrickPi.SensorType[PORT_3] = TYPE_SENSOR_COLOR_RED
##BrickPi.SensorType[PORT_3] = TYPE_SENSOR_COLOR_FULL
##BrickPi.SensorType[PORT_4] = TYPE_SENSOR_ULTRASONIC_CONT



BrickPiSetupSensors()

def motor(port, speed):
    BrickPi.MotorSpeed[port] = speed
    BrickPiUpdateValues()

def motorall(speed):
    BrickPi.MotorSpeed[PORT_A] = speed
    BrickPi.MotorSpeed[PORT_B] = speed
    BrickPi.MotorSpeed[PORT_C] = speed
    BrickPi.MotorSpeed[PORT_D] = speed
    BrickPiUpdateValues()

def motorenable():
    BrickPi.MotorEnable[PORT_A] = 1
    BrickPi.MotorEnable[PORT_B] = 1
    BrickPi.MotorEnable[PORT_C] = 1
    BrickPi.MotorEnable[PORT_D] = 1

def motordisable():
    BrickPi.MotorEnable[PORT_A] = 0
    BrickPi.MotorEnable[PORT_B] = 0
    BrickPi.MotorEnable[PORT_C] = 0
    BrickPi.MotorEnable[PORT_D] = 0

def touchenable(p1, p2):
    BrickPi.SensorType[p1] = TYPE_SENSOR_TOUCH
    BrickPi.SensorType[p2] = TYPE_SENSOR_TOUCH

def colorblue():
    BrickPi.SensorType[PORT_3] = TYPE_SENSOR_COLOR_BLUE
    BrickPiSetupSensors()
    BrickPiUpdateValues()
    
def colorred():
    BrickPi.SensorType[PORT_3] = TYPE_SENSOR_COLOR_RED
    BrickPiSetupSensors()
    BrickPiUpdateValues()
    
def colorgreen():
    BrickPi.SensorType[PORT_3] = TYPE_SENSOR_COLOR_GREEN
    BrickPiSetupSensors()
    BrickPiUpdateValues()
    
