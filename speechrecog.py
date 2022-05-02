# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 19:22:18 2022

@author: Quantum Sage
"""

import SpeechRecognition as sr

audio_file=("sample.voice.wav")

r=sr.Recognizer()

with sr.AudioFile(audio_file) as source:
    audio=r.record(source)

try:
    print(r.recognize_google(audio))
except sr.UnknownValueError:
    print("Cant decipher")
except sr.RequestError:
    print("cant connect to google")
    