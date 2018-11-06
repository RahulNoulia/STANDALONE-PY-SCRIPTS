
from gtts import *

"""

  gTTs is a Google text=to-speech API which is very easy to use and convert entered  text to voice 

  you can install gTTs API  by  typing this command ( pip3 install gTTS  )

"""

import os


mytext = input()

language = 'en'


myobj = gTTS(text=mytext, lang=language, slow=True)   # here you can also give false to slow    -> slow =false

myobj.save("myaudio.mp3")

os.system("mpg321 myaudio.mp3")   # it save this mp3 file in your current directory where you execute the script


"""
  if mpg321 is not installed than install it  by typing the command in  terminal ->  apt-get install mpg321

  mpg321 is a very popular command-line mp3 player

"""
