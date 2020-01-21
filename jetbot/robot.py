import time
import traitlets
from traitlets.config.configurable import SingletonConfigurable
from .MegaRover_MotorDriver import MegaRover_MotorDriver
from .motor import Motor


class Robot(SingletonConfigurable):

    left_motor = traitlets.Instance(Motor)
    right_motor = traitlets.Instance(Motor)

    # config
    left_motor_channel = traitlets.Integer(default_value=1).tag(config=True)
    left_motor_alpha = traitlets.Float(default_value=1.0).tag(config=True)
    right_motor_channel = traitlets.Integer(default_value=2).tag(config=True)
    right_motor_alpha = traitlets.Float(default_value=1.0).tag(config=True)

    def __init__(self, *args, **kwargs):
        super(Robot, self).__init__(*args, **kwargs)
        self.motor_driver = MegaRover_MotorDriver()
        self.right_motor = Motor(self.motor_driver, channel=self.right_motor_channel, alpha=self.right_motor_alpha)
        self.left_motor = Motor(self.motor_driver, channel=self.left_motor_channel, alpha=self.left_motor_alpha)

    def set_motors(self, left_speed, right_speed):
        self.left_motor._write_value(left_speed)
        self.right_motor._write_value(right_speed)

    def forward(self, speed=1.0, duration=None):
        self.left_motor._write_value(speed)
        self.right_motor._write_value(speed)

    def backward(self, speed=1.0):
        self.left_motor._write_value(-speed)
        self.right_motor._write_value(-speed)

    def left(self, speed=1.0):
        self.left_motor._write_value(-speed)
        self.right_motor._write_value(speed)

    def right(self, speed=1.0):
        self.left_motor._write_value(speed)
        self.right_motor._write_value(-speed)

    def stop(self):
        self.left_motor._write_value(0)
        self.right_motor._write_value(0)
