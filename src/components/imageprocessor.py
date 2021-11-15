from PIL import Image
from numpy import array
import cv2

class ImageProcessor:
    def __init__(self):
        pass
    
    @staticmethod
    def pillowImageToCV(img):
        return cv2.cvtColor(array(img), cv2.COLOR_RGB2BGR)

    @staticmethod
    def toBin(img):
        img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        (thresh, img)=cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
        return img
    
    @staticmethod
    def displayImg(img):
        cv2.imshow("image", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
