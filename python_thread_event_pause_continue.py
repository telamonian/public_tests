#!/usr/bin/env python
"""Written for https://stackoverflow.com/q/49837500/425458
"""
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
    i = 0
    while isRunning:
        event.wait(1)

        if event.isSet() and isRunning:
            event.clear()
            print('Pausing count at %d' % i)
            event.wait()
            print('resuming count')
            event.clear()

        i += 1

def listener(event):
    # in Python, need to mark globals if writing to them
    global isRunning

    while isRunning:
        c = getch()
        if c=='a':
            event.set()
        if c=='e':
            event.set()
            isRunning = False

def main():
    pauseEvent = Event()
    pauseEvent.clear()

    listenerThread = Thread(target=listener, args=(pauseEvent,))

    listenerThread.start()
    count(pauseEvent)

if __name__=='__main__':
    main()

