#All Imports#
from __future__ import print_function
from __future__ import division
from builtins import input
import time
import func
from BrickPi import *
from Expert_Mode import ExpertMode

#BrickPi Activation#
BrickPiSetup()

func.motorenable()
func.touchenable(PORT_1, PORT_2)

BrickPiSetupSensors()

#Lists#
options =  ['1. Test Components', '2. Expert Mode']
components = ['1. Motors', '2. Touch', '3. Color', '4. Light', '5. Ultrasonic']
colors = ['1. Red', '2. Green', '3. Blue', '4. Spazm']
col = [ None , "Black","Blue","Green","Yellow","Red","White" ]

#All the Testing functions#
def MotorTest():
    func.motorenable()
    print ("Testing Motors...")
    power = 100
    func.motorall(power)
    st = time.time()
    while (time.time() - st < 5):
        BrickPiUpdateValues()
    print ("Done!")

def TouchTest():
    func.motordisable()
    print ('Testing Touch...')
    st = time.time()
    while (time.time() - st < 5):
        BrickPiUpdateValues()
        First = BrickPi.Sensor[PORT_1]
        First2 = BrickPi.Sensor[PORT_2]
        print(str(First) + '    ' + str(First2))
        BrickPiUpdateValues()
        Secound = BrickPi.Sensor[PORT_1]
        Secound2 = BrickPi.Sensor[PORT_2]
        if First == Secound:
            pass
        else:
            print (str(Secound) + '    ' + str(Secound2))
        time.sleep(0.5)
    print ('Done!')

def ColorTest():
    st = time.time()
    while time.time() - st < 10:
        func.colorred()
        func.colorgreen()
        func.colorblue()
    print ('Done!')
    BrickPi.SensorType[PORT_3] = TYPE_SENSOR_COLOR_NONE
    BrickPiSetupSensors()
    BrickPiUpdateValues()

def LightTest():
    print ('Testing...')
    BrickPi.SensorType[PORT_3] = TYPE_SENSOR_COLOR_FULL
    BrickPiSetupSensors()
    st = time.time()
    while time.time() - st < 5:
        BrickPiUpdateValues()
        print (col[BrickPi.Sensor[PORT_3]])
        time.sleep(0.5)
    BrickPi.SensorType[PORT_3] = TYPE_SENSOR_COLOR_NONE
    BrickPiSetupSensors()
def UltraTest():
    BrickPi.SensorType[PORT_4] = TYPE_SENSOR_ULTRASONIC_CONT
    BrickPiSetupSensors()
    st = time.time()
    while time.time() - st < 5:
        BrickPiUpdateValues()
        print (BrickPi.Sensor[PORT_4])
        time.sleep(0.1)

#All the Answer Processing Functions#
def AnsProcessing(oa):
    optlen = len(options)
    new_oa = int(oa)
    if 0 < new_oa < (optlen + 1):
        return options[new_oa - 1]
    else:
        print ('Invalid Statment')

def AnsProcessing2(ab):
    if ab == options[0]:
        print ('\n')
        print ('Components Options')
        print ('\n'.join(map(str, components)))
        while True:
            answer_middle = input ("Enter the Number for the action you want:")
            check = IntCheck(answer_middle)
            if check == 'g':
                answer_end = AnsProcessing3(answer_middle)
                return answer_end
            else:
                print('Invalid Statement')
    if ab == options[1]:
        coming = 'y'
        return coming

def AnsProcessing3(a):
    comlen = len(components)
    new_a = int(a)
    if 0 < new_a < (comlen + 1):
        return components[new_a - 1]
    else:
        print ('Invalid Statment')

#All the Other Functions#
def MainMenu():
    print ('\n')
    print ('Main Menu Options')
    print ('\n'.join(map(str, options)))
    while True:
        old_answer = input ("Enter the Number for the action you want:")
        check = IntCheck(old_answer)
        if check == 'g':
            old_answer_new = AnsProcessing(old_answer)
            return old_answer_new
        else:
            print('Invalid Statement')

def IntCheck(variable):
    try:
        new = int(variable)
        return 'g'
    except ValueError:
        return 'b'

#Start Code#
print ("Welcome to the Brick Pi Testing!")
print ('''
Make sure that the motors are on ports:
M1
M2
M3

The touch sensors on ports:
S1
S2

The color sensor on port:
S3

The ultrasonic sensor on port:
S4
''')


time.sleep(0.5)
whichtest = 'null'

while True:
    whichtest = 'null'
    answer_before = MainMenu()
    answer = AnsProcessing2(answer_before)
    if answer == 'y':
        whichtest = 'mas'
    if answer == components[0]:
        MotorTest()
        whichtest = 'M'

    if answer == components[1]:
        TouchTest()
        whichtest = 'T'

    if answer == components[2]:
        ColorTest()
        whichtest = 'C'

    if answer == components[3]:
        LightTest()
        whichtest = 'L'

    if answer == components[4]:
        UltraTest()
        whichtest = 'U'

    if whichtest == 'mas':
        print ('Expert Mode On')
        ExpertMode()
        confirmation = 'n'
    else:    
        confirmation = input('Do you want to repeat the test? [y/n]')
        
    while (confirmation == 'y'):
        if whichtest == 'M':
            MotorTest()

        if whichtest == 'T':
            TouchTest()

        if whichtest == 'C':
            ColorTest()

        if whichtest == 'L':
            LightTest()

        if whichtest == 'U':
            UltraTest()
        confirmation = input('Do you want to repeat your test? [y/n]')

    stop = input('Do you want to test something else? [y/n]')
    if stop == 'y':
        pass
    elif stop == 'n':
        break
print ('Goodbye')
