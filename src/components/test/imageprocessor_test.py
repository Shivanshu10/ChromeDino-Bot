import sys
sys.path.append('../')
from imageprocessor import ImageProcessor
from PIL import Image

img=Image.open("sample.png")
imgp=ImageProcessor()
img=imgp.pillowImageToCV(img)
img=imgp.toBin(img)
imgp.displayImg(img)
