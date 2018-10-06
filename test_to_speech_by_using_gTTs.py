
from gtts import *

#  gTTs is a Google text=to-speech API which is very easy to use convert entered  text to voice (  by saving it in mp3 format )

#  you can install gTTs API  by  typing this command ( pip install gTTS  )

import os


mytext = input()

language = 'en'


myobj = gTTS(text=mytext, lang=language, slow=True)   # here you can also give false to slow    -> slow =false

myobj.save("welcome.mp3")

os.system("mpg321 myaudio.mp3")   # it save this mp3 file to your current directory where you execute your script



#  if mpg321 is not installed than install by typing in  terminal ->  apt-get install mpg321

#  mpg321 is a very popular command-line mp3 player
