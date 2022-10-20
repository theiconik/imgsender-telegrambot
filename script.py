import os
import glob
from telegram_part import *

dict = {}
flag = False
# * matches all files in directory
# if you need other specific file types
# use *.[type], for example *.py
while(True):
    file_location = ""
    files_in_dir = glob.glob(file_location + "*.png")
    recent_file = max(files_in_dir, key=os.path.getctime)
    # find in map
    if recent_file in dict:
       continue
    else:
       try:
          sendPhotoOnTelegram(recent_file)
       except:
          print("Some error occured while sending photo!")
          flag = True

       if flag:
          break
       dict[recent_file] = True
