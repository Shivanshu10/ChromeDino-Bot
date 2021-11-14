import sys
sys.path.append('../')
from controller import Controller
import time

controller=Controller()
controller.openDino(1)
time.sleep(3)
controller.closeDino(0)