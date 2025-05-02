from DM_CAN import *
import numpy as np
import time
import serial
import math

Motor1 = Motor(DM_Motor_Type.DM4310,0x01,  0x11)

serial_device = serial.Serial(
    port='COM3',
    baudrate=921600,
    timeout=0.5
)
MotorControl1 = MotorControl(serial_device)
print("1")
MotorControl1.addMotor(Motor1)
print("2")
MotorControl1.enable_old(Motor1, Control_Type.VEL)
print("4")
time.sleep(3)
q = math.sin(time.time())
MotorControl1.control_Vel(Motor1, q*5)
print("5")
time.sleep(1)
print("6")
MotorControl1.refresh_motor_status(Motor1)
print("Motor1:", "POS:", Motor1.getPosition(), "VEL:", Motor1.getVelocity(), "TORQUE:", Motor1.getTorque())

MotorControl1.disable(Motor1)