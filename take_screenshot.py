# this file requires installation of python 2.5+ or 3.x
# Python Imaging Library (PIL) python-imaging installation
# google tesseract ocr installation

#import subprocess as sp
# subprocess module is used to run commands of shell...
# in python script.

# module to take screenshot via python script
import pyscreenshot as SS
# module to extract text from the image
from pytesseract import image_to_string as ItoS
# to hold the program execution
import time

# to take screen shot via shell
# import -window root screen.png
# sp.call(["import", "-window", "root", "screen.png"])

# hold execution for few seconds
time.sleep(5)
# capture the current screenshot
image = SS.grab()
# display the image
#image.show()
# save the image file
#image.save('screenshot.png')
# read the contents of the image file stored in PIL memory
text = ItoS(image, lang='eng')

# open the file for writing the text
file_obj = open('screen_input', 'w')
# write extracted text from image to the file
file_obj.write(text.encode('utf-8'))
# close the file
file_obj.close()
