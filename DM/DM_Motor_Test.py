import math
from DM_CAN import *
import serial
import time


Motor1=Motor(DM_Motor_Type.DM4310,0x01,0x11)
Motor2=Motor(DM_Motor_Type.DM4310,0x05,0x15)
serial_device = serial.Serial('COM3', 921600, timeout=0.5)
MotorControl1=MotorControl(serial_device)
MotorControl1.addMotor(Motor1)
MotorControl1.addMotor(Motor2)


# MotorControl1.enable(Motor3)
MotorControl1.save_motor_param(Motor1)
MotorControl1.save_motor_param(Motor2)
MotorControl1.enable(Motor1)
MotorControl1.enable(Motor2)
i=0
while i<30000:
    q=math.sin(time.time())
    i=i+1
    # MotorControl1.control_pos_force(Motor1, 10, 1000,100)
    # MotorControl1.control_Vel(Motor1, q*5)
    MotorControl1.controlMIT(Motor1,30, 0.8, 8*q, 0, 0)
    # MotorControl1.controlMIT(Motor1, 50, 0.3, q, 0, 0)
    # print("Motor1:","POS:",Motor1.getPosition(),"VEL:",Motor1.getVelocity(),"TORQUE:",Motor1.getTorque())
    # MotorControl1.controlMIT(Motor2, 35, 0.1, 8*q, 0, 0)

    # MotorControl1.control_Vel(Motor2, 8*q)
    # print("Motor2:","POS:",Motor2.getPosition(),"VEL:",Motor2.getVelocity(),"TORQUE:",Motor2.getTorque())
    # print(Motor1.getTorque())
    # print(Motor2.getTorque())
    time.sleep(0.01)
    # MotorControl1.control(Motor3, 50, 0.3, q, 0, 0)


MotorControl1.disable(Motor1)
#语句结束关闭串口
serial_device.close()