from m5stack import *
from m5ui import *
from uiflow import *
import imu

setScreenColor(0x222222)



imu0 = imu.IMU()
FREE = M5TextBox(62, 157, "FREE", lcd.FONT_DejaVu72,0x04ff00, rotate=0)
BUSY = M5TextBox(251, 83, "BUSY", lcd.FONT_DejaVu72,0xff0000, rotate=180)
lunch = M5TextBox(39, 88, "LUNCH", lcd.FONT_DejaVu72,0xf3ff00, rotate=0)

state = None
button = None


def buttonA_wasPressed():
  global state, button
  state = 2
  button = 1
  pass
btnA.wasPressed(buttonA_wasPressed)

def buttonC_wasPressed():
  global state, button
  state = 0
  button = 0
  pass
btnC.wasPressed(buttonC_wasPressed)


state = 0
button = 0
while True:
  if state == 0:
    FREE.show()
    BUSY.hide()
    lunch.hide()
    button = 0
  elif state == 1:
    FREE.hide()
    BUSY.show()
    lunch.hide()
    button = 0
  elif state == 2:
    FREE.hide()
    BUSY.hide()
    lunch.show()
    button = 1
  if state == 0:
    rgb.setColorAll(0x33ff33)
  elif state == 1:
    rgb.setColorAll(0xff0000)
  elif state == 2:
    rgb.setColorAll(0xffff00)
  if button == 0:
    if (imu0.acceleration[0]) < -0.012:
      state = 1
    elif (imu0.acceleration[0]) > -0.012:
      state = 0
  else:
    pass
  wait_ms(2)
