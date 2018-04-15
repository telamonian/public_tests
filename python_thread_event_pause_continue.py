#!/usr/bin/env python
from threading import Thread, Event
import time

def count(pauseEvent, continueEvent):
    i = 0
    while True:
        time.sleep(2)
        i += 1
        
        if listenPause.isSet():
            pauseCount(i, continueEvent)

def pauseCount(i, continueEvent):
    print('Pausing count at %d' % i)
    continueEvent.wait()
    print('resuming count')
    return
            
def listenPause(pauseEvent, continueEvent):
    continueEvent.clear()
    
    while True:
        s = raw_input("Enter 'a' for pause")
        if s=='a':
            pauseEvent.set()
            return

def listenContinue(pauseEvent, continueEvent):
    pauseEvent.clear()
    
    while True:
        s = raw_input("Enter 'a' for continue")
        if s=='a':
            continueEvent.set()
            return
        
def listener(pauseEvent, continueEvent):
    while True:
        listenPause(pauseEvent, continueEvent)
        listenContinue(pauseEvent, continueEvent)

def main():
    pauseEvent = Event()
    continueEvent = Event()
    
    listenerThread = Thread(target=listener, args=(pauseEvent, continueEvent))
    
    listenerThread.start()
    count()
    
main()
