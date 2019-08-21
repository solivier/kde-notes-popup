#!/usr/bin/python
import notify2
import random

f=open("notes.txt", "r")

if f.mode == 'r':
    contents =f.read()
    notes = contents.split("---")

notify2.init('Random note!')
n = notify2.Notification('Random note!', notes[random.randrange(len(notes))]) 
n.timeout = 30000
n.show()

