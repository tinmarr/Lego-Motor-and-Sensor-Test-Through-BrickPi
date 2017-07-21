#All Imports#
from __future__ import print_function
from __future__ import division
from builtins import input
import time
import func
from BrickPi import *

#BrickPi Activation#
BrickPiSetup()

func.motorenable()
func.touchenable(PORT_1, PORT_2)

BrickPiSetupSensors()

def ExpertMode():
    #Lists#
    components = ['1. Motors', '2. Touch', '3. Color', '4. Light', '5. Ultrasonic']
    colors = ['1. Red', '2. Green', '3. Blue', '4. Spazm']
    col = [ None , "Black","Blue","Green","Yellow","Red","White" ]
    motors = ['1. Motor A', '2. Motor B', '3. Motor C', '4. Motor D', '5. All Motors']

   #All the Testing functions#
    def MotorTest():
        func.motorenable()
        print ('\n')
        print ('Motor Options')
        print ('\n'.join(map(str, motors)))
        while True:
            motornum_raw = input('Which Motor Number?')
            check = IntCheck(motornum_raw)
            if check == 'g':
                motornumber = AnsProcessing(motornum_raw, motors)
                while True:
                    powe = input('What Speed?')
                    check = IntCheck(powe)
                    if check == 'g':
                        power = int(powe)
                        print ("Testing Motor(s)...")
                        st = time.time()
                        while (time.time() - st < 5):
                            if motornumber == motors[0]:
                                func.motor(PORT_A, power)            

                            if motornumber == motors[1]:
                                func.motor(PORT_B, power)

                            if motornumber == motors[2]:
                                func.motor(PORT_C, power)

                            if motornumber == motors[3]:
                                func.motor(PORT_D, power)

                            if motornumber == motors[4]:
                                func.motorall(power)
                        print ("Done!")
                        break
                    else:
                        print('Invalid Statment')
            else:
                print('Invalid Statement')
            
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
        while True:
            print ('\n'.join(map(str, colors)))
            color = input('What Color Number?')
            check = IntCheck(color)
            if check == 'g':
                collen = len(colors)
                new_col = int(color)
                if 0 < new_col < (collen + 1):
                    the_color = colors[new_col - 1]
                    if the_color == colors[0]:
                        print ('Testing ' + the_color + '...')
                        BrickPi.SensorType[PORT_3] = TYPE_SENSOR_COLOR_RED
                        BrickPiSetupSensors()
                        st = time.time()
                        while time.time() - st < 5:
                            BrickPiUpdateValues()
                        print ('Done!')
                    if the_color == colors[1]:
                        print ('Testing ' + the_color + '...')
                        BrickPi.SensorType[PORT_3] = TYPE_SENSOR_COLOR_GREEN
                        BrickPiSetupSensors()
                        st = time.time()
                        while time.time() - st < 5:
                            BrickPiUpdateValues()
                        print ('Done!')
                    if the_color == colors[2]:
                        print ('Testing ' + the_color + '...')
                        BrickPi.SensorType[PORT_3] = TYPE_SENSOR_COLOR_BLUE
                        BrickPiSetupSensors()
                        st = time.time()
                        while time.time() - st < 5:
                            BrickPiUpdateValues()
                        print ('Done!')
                    if the_color == colors[3]:
                        print ('Testing ' + the_color + '...')
                        st = time.time()
                        while time.time() - st < 10:
                            func.colorred()
                            func.colorgreen()
                            func.colorblue()
                        print ('Done!')
                BrickPi.SensorType[PORT_3] = TYPE_SENSOR_COLOR_NONE
                BrickPiSetupSensors()
                BrickPiUpdateValues()
            else:
                print('Invalid Statment')

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

    def IntCheck(variable):
        try:
            new = int(variable)
            return 'g'
        except ValueError:
            return 'b'

    #All the Answer Processing Functions#
    def AnsProcessing(oa, listname):
        lislen = len(listname)
        new_oa = int(oa)
        if 0 < new_oa < (lislen + 1):
            return listname[new_oa - 1]
        else:
            print ('Invalid Statment')
            
    def AnsProcessing2():
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
                
    def AnsProcessing3(a):
        comlen = len(components)
        new_a = int(a)
        if 0 < new_a < (comlen + 1):
            return components[new_a - 1]
        else:
            print ('Invalid Statment')

    #Start Code#
    while True:
        whichtest = 'null'
        answer = AnsProcessing2()
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

        stop = input('Do you want to test something else in Expert Mode? [y/n]')
        if stop == 'y':
            pass
        elif stop == 'n':
            break
