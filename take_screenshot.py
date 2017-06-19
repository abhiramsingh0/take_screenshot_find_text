# this file requires installation of python 2.5+ or 3.x
# Python Imaging Library (PIL) python-imaging installation
# google tesseract ocr installation

# import subprocess as sp
# subprocess module is used to run commands of shell...
# in python script.

# module to take screenshot via python script
import pyscreenshot as SS
# module to extract text from the image
from pytesseract import image_to_string as ItoS
# to hold the program execution
#import time
# to treat file as string objects
import mmap
# import os module to print error message
import os
# import errno module to print errer messages
import errno
# import system libraray 
from sys import exit

# to take screen shot via shell
# import -window root screen.png
# sp.call(["import", "-window", "root", "screen.png"])

# hold execution for few seconds
#time.sleep(5)
# capture the current screenshot
image = SS.grab()
# display the image
#image.show()
# save the image file
#image.save('screenshot.png')
# read the contents of the image file stored in PIL memory
text = ItoS(image, lang='eng')

# open the file for writing the text
try:
  file_obj = open('screen_input', 'w+')
except IOError as ioex:
  print "error no:", ioex.errno
  print "err code:", errno.errorcode[ioex.errno]
  print "err msg:", os.strerror(ioex.errno)
  # cleanup the code
  exit()
# write extracted text from image to the file
file_obj.write(text.encode('utf-8'))
# bring the control to the starting of file
file_obj.seek(0)
# create mmap object to treat file as string
try:
  mmap_obj = mmap.mmap(file_obj.fileno(), 0)
except IOError as ioex:
  print "error no:", ioex.errno
  print "err code:", errno.errorcode[ioex.errno]
  print "err msg:", os.strerror(ioex.errno)
  # cleanup the code
  file_obj.close()
  exit()

# search for a word in mmap_obj
is_success = mmap_obj.find("execution")
if -1 == is_success:
  print "string not found in file"
else:
  print "string found"
# close the file
file_obj.close()
