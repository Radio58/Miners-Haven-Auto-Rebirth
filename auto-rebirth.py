import pyautogui as gui
import vgamepad as vg
import time

gamepad = vg.VX360Gamepad()
def dpadDown(count=1):
    i = 0
    while i < count:
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
        gamepad.update()
        time.sleep(0.05)
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
        gamepad.update()
        time.sleep(0.05)
        i += 1


def dpadRight(count=1):
    i = 0
    while i < count:
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
        gamepad.update()
        time.sleep(0.05)
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
        gamepad.update()
        time.sleep(0.05)
        i += 1

def pressA(count=1):
    i = 0
    while i < count:
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
        gamepad.update()
        time.sleep(0.05)
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
        gamepad.update()
        time.sleep(0.05)
        i += 1

def pressB(count=1):
    i = 0
    while i < count:
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
        gamepad.update()
        time.sleep(0.05)
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
        gamepad.update()
        time.sleep(0.05)
        i += 1

def openMenu():
    dpadRight(2)
    dpadDown()
    pressA()

def loadLayout():
    openMenu()
    
    # Button presses to load saved layout 3
    dpadDown(3)
    pressA()
    dpadDown(4)
    dpadRight()
    pressA()
    pressB()

def tryRebirth():
    openMenu()

    # Check if rebirth indicator is fully green, returns if not
    try:
        indicator = gui.locateCenterOnScreen('images/indicator.png')
    except gui.ImageNotFoundException:
        print('cannot rebirth')
        pressB()
        return
    
    # Brings up rebirth confirmation
    dpadDown()
    pressA()

    # Determines whether the yes button is on the right or left and rebirths
    try:
        confirm = gui.locateCenterOnScreen('images/yes-right.png')
        dpadRight()
        pressA()
        loadLayout()
        return
    except gui.ImageNotFoundException:
        pass
    
    try:
        confirm = gui.locateCenterOnScreen('images/yes-left.png')
        pressA()
        loadLayout()
        return
    except gui.ImageNotFoundException:
        print('could not find button')


time.sleep(3)

loadLayout()
while True:
    # Activate controller mode by pressing down.
    dpadDown()

    tryRebirth()

    time.sleep(5)