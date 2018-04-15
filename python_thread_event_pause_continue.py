#!/usr/bin/env python
import os
from threading import Thread, Event

if os.name=='nt':
    from msvcrt import getch
elif os.name=='posix':
    from getch import getch
else:
    raise OSError

isRunning = True

def count(event):
    global isRunning

    i = 0
    while isRunning:
        event.wait(2)

        if event.isSet() and isRunning:
            event.clear()
            print('Pausing count at %d' % i)
            event.wait()
            print('resuming count')
            event.clear()

        i += 1

def _listener(event, msg):
    global isRunning

    while True:
        c = getch()
        if c=='a':
            event.set()
            return
        if c=='e':
            event.set()
            isRunning = False
            return

def listener(event):
    msg,nextMsg = "Enter 'a' for pause", "Enter 'a' for continue"

    while isRunning:
        _listener(event, msg=msg)
        msg,nextMsg = nextMsg,msg

def main():
    pauseEvent = Event()
    pauseEvent.clear()

    listenerThread = Thread(target=listener, args=(pauseEvent,))

    listenerThread.start()
    count(pauseEvent)

main()
