import pyautogui
import time

class Controller:
    def __init__(self, t, w):
        self.t=t
        self.w=w

    def look(self):
        return pyautogui.screenshot(region=(0, self.t, pyautogui.size()[0]-self.w, pyautogui.size()[1]-self.t))
    
    def takeSS(self, x, y, w, h):
        return pyautogui.screenshot(region=(x, y, w, h))

    def pressKey(self, key):
        pyautogui.press(key)
    
    def openDino(self, br):
        with pyautogui.hold('win'):
            pyautogui.press('r')
        pyautogui.write('chrome')
        pyautogui.press('enter')
        time.sleep(br)
        pyautogui.write('chrome://dino/')
        pyautogui.press('enter')
    
    def closeDino(self, points):
        with pyautogui.hold('alt'):
            pyautogui.press('f4')
        print("Points:" + str(points))