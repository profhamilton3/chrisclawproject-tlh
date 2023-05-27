joystickbit.onButtonEvent(joystickbit.JoystickBitPin.P12, joystickbit.ButtonType.up, function () {
    wuKong.mecanumWheel(
    wuKong.ServoList.S1,
    wuKong.ServoList.S2,
    wuKong.ServoList.S3,
    wuKong.ServoList.S4
    )
    wuKong.mecanumRun(wuKong.RunList.stop, 20)
})
joystickbit.onButtonEvent(joystickbit.JoystickBitPin.P14, joystickbit.ButtonType.down, function () {
    wuKong.mecanumWheel(
    wuKong.ServoList.S1,
    wuKong.ServoList.S2,
    wuKong.ServoList.S3,
    wuKong.ServoList.S4
    )
    wuKong.mecanumRun(wuKong.RunList.rear, 20)
})
joystickbit.onButtonEvent(joystickbit.JoystickBitPin.P13, joystickbit.ButtonType.up, function () {
    wuKong.mecanumWheel(
    wuKong.ServoList.S1,
    wuKong.ServoList.S2,
    wuKong.ServoList.S3,
    wuKong.ServoList.S4
    )
    wuKong.mecanumRun(wuKong.RunList.stop, 20)
})
input.onButtonPressed(Button.A, function () {
    wuKong.setMotorSpeed(wuKong.MotorList.M2, 10)
    basic.pause(2000)
    wuKong.stopMotor(wuKong.MotorList.M2)
})
joystickbit.onButtonEvent(joystickbit.JoystickBitPin.P15, joystickbit.ButtonType.down, function () {
    wuKong.mecanumWheel(
    wuKong.ServoList.S1,
    wuKong.ServoList.S2,
    wuKong.ServoList.S3,
    wuKong.ServoList.S4
    )
    wuKong.mecanumRun(wuKong.RunList.right, 20)
})
input.onPinPressed(TouchPin.P2, function () {
    wuKong.setServoAngle(wuKong.ServoTypeList._360, wuKong.ServoList.S6, -5)
    basic.pause(1000)
})
joystickbit.onButtonEvent(joystickbit.JoystickBitPin.P15, joystickbit.ButtonType.up, function () {
    wuKong.mecanumWheel(
    wuKong.ServoList.S1,
    wuKong.ServoList.S2,
    wuKong.ServoList.S3,
    wuKong.ServoList.S4
    )
    wuKong.mecanumRun(wuKong.RunList.stop, 20)
})
input.onButtonPressed(Button.B, function () {
    wuKong.setMotorSpeed(wuKong.MotorList.M2, -10)
    basic.pause(2000)
    wuKong.stopMotor(wuKong.MotorList.M2)
})
input.onPinPressed(TouchPin.P1, function () {
    wuKong.setServoAngle(wuKong.ServoTypeList._360, wuKong.ServoList.S6, 5)
    basic.pause(1000)
})
joystickbit.onButtonEvent(joystickbit.JoystickBitPin.P14, joystickbit.ButtonType.up, function () {
    wuKong.mecanumWheel(
    wuKong.ServoList.S1,
    wuKong.ServoList.S2,
    wuKong.ServoList.S3,
    wuKong.ServoList.S4
    )
    wuKong.mecanumRun(wuKong.RunList.stop, 20)
})
joystickbit.onButtonEvent(joystickbit.JoystickBitPin.P13, joystickbit.ButtonType.down, function () {
    wuKong.mecanumWheel(
    wuKong.ServoList.S1,
    wuKong.ServoList.S2,
    wuKong.ServoList.S3,
    wuKong.ServoList.S4
    )
    wuKong.mecanumRun(wuKong.RunList.Front, 20)
})
joystickbit.onButtonEvent(joystickbit.JoystickBitPin.P12, joystickbit.ButtonType.down, function () {
    wuKong.mecanumWheel(
    wuKong.ServoList.S1,
    wuKong.ServoList.S2,
    wuKong.ServoList.S3,
    wuKong.ServoList.S4
    )
    wuKong.mecanumRun(wuKong.RunList.left, 20)
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    wuKong.setMotorSpeed(wuKong.MotorList.M1, 10)
    basic.pause(1000)
    wuKong.stopMotor(wuKong.MotorList.M1)
})
input.onLogoEvent(TouchButtonEvent.Released, function () {
    wuKong.setMotorSpeed(wuKong.MotorList.M1, -10)
    basic.pause(1000)
    wuKong.stopMotor(wuKong.MotorList.M1)
})
basic.showIcon(IconNames.Ghost)
radio.setGroup(102)
radio.setTransmitPower(7)
wuKong.mecanumWheel(
wuKong.ServoList.S1,
wuKong.ServoList.S2,
wuKong.ServoList.S3,
wuKong.ServoList.S4
)
