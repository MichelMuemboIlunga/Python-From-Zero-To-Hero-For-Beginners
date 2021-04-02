import random as rd

# random
num = rd.randint(0, 10)
print(num)
print("-------------- Done -------------------")

# my mood Today


my_mood = ("happy", "sad", "angry")
mood = rd.choice(my_mood)

if mood == "happy":
    print("😁 happy")
elif mood == "sad":
    print("😒 sad")
elif mood == "angry":
    print("😡 angry")
else:
    print("i am not happy,not sad,not angry")
print("-------------- Done -------------------")

# http library

from http import HTTPStatus

result = HTTPStatus.NOT_FOUND.real
print(result)
print("-------------- Done -------------------")

# operating system

import os

cwd = os.getcwd()
print(cwd)
print("-------------- Done -------------------")


# speech

# import pyttsx3  # pip install pyttsx3

def say_hi():
    name = input("Please Enter Your name: ")
    age = int(input("Please Enter your age: "))
    gender = input("Please Enter Your gender: ")
    pyttsx3.speak(f'Hi, {name} you are {age} years old  and you are a {gender}')


say_hi()
print("-------------- Done -------------------")

# calendar and date

import calendar
import datetime

today = datetime.datetime.now()
Date = today.strftime("%m/%d/%Y, %H:%M:%S")
print("=================================")
print("Today's date is:", Date, "✔")
print("=================================")
print(calendar.calendar(2021))
print("-------------- Done -------------------")

# time

import time

start_time = time.time()

colors = ["red", "green", "blue", "purple", "yellow"]
i = 0
while i < len(colors):
    print(colors[i])
    i += 1

# sleeping for 5 to get some runtime
time.sleep(5)

# end time
end_time = time.time()

# total time taken
print(f"This program took {end_time - start_time}")
print("-------------- Done -------------------")

# whatshap testing send message
import pywhatkit

pywhatkit.sendwhatmsg('+27842011670', 'testing python script: If you get This message That means my python program is '
                                      'working\n Michel Muembo', 22, 20)


title = "Isaiah 53:2-4"
text = "2. He grew up before him like a tender shoot,\n and like a root out of dry ground.\n" \
       "He had no beauty or majesty to attract us to him,\n" \
       "nothing in his appearance that we should desire him.\n\n" \
       "3. He was despised and rejected by mankind,\n" \
       "a man of suffering, and familiar with pain.\n" \
       "Like one from whom people hide their faces\n" \
       "he was despised, and we held him in low esteem.\n\n" \
       "4 Surely he took up our pain\n" \
       "and bore our suffering,\n" \
       "yet we considered him punished by God,\n" \
       "stricken by him, and afflicted."

m = pywhatkit.text_to_handwriting(title + text, rgb=[172, 6, 167, 1])
result = str(m)
print(type(result))
print(result)

pywhatkit.sendwhatmsg('+27842011670', m, 11, 32)
print("-------------- Done -------------------")
# web browser

import webbrowser

webbrowser.open("https://www.linkedin.com/in/muembo-ilunga-michel-b707b518b/")


# play music

from playsound import playsound
playsound('05 AKUMISAMA.mp3')


# opening url and display the code source

import urllib.request

try:
    with urllib.request.urlopen('https://docs.python.org/3/library/urllib.request.html') as f:
        print(f.read().decode('utf-8'))
except urllib.error.URLError as e:
    print(e.reason)
print("-------------- Done -------------------")

# conversation

import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 130)
engine.setProperty('voice', voices[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


speak("What do you want me to say?")


while True:
    word = input("==> ")
    if word == "exit":
        exit(0)
    speak(word)
    print(voices)
