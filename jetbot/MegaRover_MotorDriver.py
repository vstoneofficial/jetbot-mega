import  serial
import  struct

class MegaRover_DCMotor:
    #�e���[�^�̖ڕW���x�i�[�������̃A�h���X
    LEFT_MOTOR = 'AC'
    RIGHT_MOTOR = 'AE'

    def __init__(self,driver,motornum):
        self.ser = driver

        if motornum == 0:
            self.motorAddr = self.LEFT_MOTOR
        elif motornum == 1:
            self.motorAddr = self.RIGHT_MOTOR
        else:
            raise NameError('Motor chennel must be between 1 and 2 inclusive')

    def setSpeed(self,speed):
        if speed > 1300:
            speed=1300
        elif speed < -1300:
            speed = -1300
        cmd = 'w10 ' + self.motorAddr + ' ' + self.int2litteEndian(speed) + '\n'
        self.ser.write(cmd.encode('utf-8'))

    def int2litteEndian(self,speed):
        #���g���G���f�B�A��(2�o�C�g)�ɕϊ�
        speed_bin = struct.pack('<h',speed)
        return speed_bin.hex()


class MegaRover_MotorDriver:
    WRC_GAIN_ADDR = '20'

    def __init__(self, addr='/dev/ttyUSB_Rover', baud=115200, waitLimit=0.1, *args):
        try:
            self.ser = serial.Serial(addr,baud,timeout=waitLimit)
            self.motors = [MegaRover_DCMotor(self.ser, m) for m in range(2)]
            #���x�̔��Q�C����0�Ɂi0�ȊO�̏ꍇ�A�V���A���ő��삪�ł��Ȃ��j
            start_cmd = 'w10 ' + self.WRC_GAIN_ADDR + ' 00000000\n'
            self.ser.write(start_cmd.encode('utf-8'))
        except FileNotFoundError as e:
            print(e)

    def getMotor(self,num):
        if (num < 1) or (num > 2):
            raise NameError('MotorHAT Motor must be between 1 and 4 inclusive')
        return self.motors[num-1]
