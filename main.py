def my_function():
    wuKong.mecanum_wheel(wuKong.ServoList.S1,
        wuKong.ServoList.S2,
        wuKong.ServoList.S3,
        wuKong.ServoList.S4)
    wuKong.mecanum_run(wuKong.RunList.STOP, 20)
joystickbit.on_button_event(joystickbit.JoystickBitPin.P12,
    joystickbit.ButtonType.UP,
    my_function)

def my_function2():
    wuKong.mecanum_wheel(wuKong.ServoList.S1,
        wuKong.ServoList.S2,
        wuKong.ServoList.S3,
        wuKong.ServoList.S4)
    wuKong.mecanum_run(wuKong.RunList.REAR, 20)
joystickbit.on_button_event(joystickbit.JoystickBitPin.P14,
    joystickbit.ButtonType.DOWN,
    my_function2)

def my_function3():
    wuKong.mecanum_wheel(wuKong.ServoList.S1,
        wuKong.ServoList.S2,
        wuKong.ServoList.S3,
        wuKong.ServoList.S4)
    wuKong.mecanum_run(wuKong.RunList.STOP, 20)
joystickbit.on_button_event(joystickbit.JoystickBitPin.P13,
    joystickbit.ButtonType.UP,
    my_function3)

def on_button_pressed_a():
    wuKong.set_motor_speed(wuKong.MotorList.M2, 10)
    basic.pause(2000)
    wuKong.stop_motor(wuKong.MotorList.M2)
input.on_button_pressed(Button.A, on_button_pressed_a)

def my_function4():
    wuKong.mecanum_wheel(wuKong.ServoList.S1,
        wuKong.ServoList.S2,
        wuKong.ServoList.S3,
        wuKong.ServoList.S4)
    wuKong.mecanum_run(wuKong.RunList.RIGHT, 20)
joystickbit.on_button_event(joystickbit.JoystickBitPin.P15,
    joystickbit.ButtonType.DOWN,
    my_function4)

def on_pin_pressed_p2():
    wuKong.set_servo_angle(wuKong.ServoTypeList._360, wuKong.ServoList.S6, -5)
    basic.pause(1000)
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

def my_function5():
    wuKong.mecanum_wheel(wuKong.ServoList.S1,
        wuKong.ServoList.S2,
        wuKong.ServoList.S3,
        wuKong.ServoList.S4)
    wuKong.mecanum_run(wuKong.RunList.STOP, 20)
joystickbit.on_button_event(joystickbit.JoystickBitPin.P15,
    joystickbit.ButtonType.UP,
    my_function5)

def on_button_pressed_b():
    wuKong.set_motor_speed(wuKong.MotorList.M2, -10)
    basic.pause(2000)
    wuKong.stop_motor(wuKong.MotorList.M2)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_pin_pressed_p1():
    wuKong.set_servo_angle(wuKong.ServoTypeList._360, wuKong.ServoList.S6, 5)
    basic.pause(1000)
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

def my_function6():
    wuKong.mecanum_wheel(wuKong.ServoList.S1,
        wuKong.ServoList.S2,
        wuKong.ServoList.S3,
        wuKong.ServoList.S4)
    wuKong.mecanum_run(wuKong.RunList.STOP, 20)
joystickbit.on_button_event(joystickbit.JoystickBitPin.P14,
    joystickbit.ButtonType.UP,
    my_function6)

def my_function7():
    wuKong.mecanum_wheel(wuKong.ServoList.S1,
        wuKong.ServoList.S2,
        wuKong.ServoList.S3,
        wuKong.ServoList.S4)
    wuKong.mecanum_run(wuKong.RunList.FRONT, 20)
joystickbit.on_button_event(joystickbit.JoystickBitPin.P13,
    joystickbit.ButtonType.DOWN,
    my_function7)

def my_function8():
    wuKong.mecanum_wheel(wuKong.ServoList.S1,
        wuKong.ServoList.S2,
        wuKong.ServoList.S3,
        wuKong.ServoList.S4)
    wuKong.mecanum_run(wuKong.RunList.LEFT, 20)
joystickbit.on_button_event(joystickbit.JoystickBitPin.P12,
    joystickbit.ButtonType.DOWN,
    my_function8)

def on_logo_pressed():
    wuKong.set_motor_speed(wuKong.MotorList.M1, 10)
    basic.pause(1000)
    wuKong.stop_motor(wuKong.MotorList.M1)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def on_logo_released():
    wuKong.set_motor_speed(wuKong.MotorList.M1, -10)
    basic.pause(1000)
    wuKong.stop_motor(wuKong.MotorList.M1)
input.on_logo_event(TouchButtonEvent.RELEASED, on_logo_released)

basic.show_icon(IconNames.GHOST)
radio.set_group(102)
radio.set_transmit_power(7)
wuKong.mecanum_wheel(wuKong.ServoList.S1,
    wuKong.ServoList.S2,
    wuKong.ServoList.S3,
    wuKong.ServoList.S4)