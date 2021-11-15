import sys
sys.path.append('../')
from controller import Controller
import time
from PIL import Image

controller=Controller(100, 1000)
controller.openDino(1)
time.sleep(1)
controller.pressKey('space')
time.sleep(2)
img=controller.look()
img.save('dino.png')
time.sleep(3)
controller.closeDino(0)