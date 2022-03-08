#!usr/bin/env python

import sys
import MySQLdb
from threading import Thread
import threading
import time
import RPi.GPIO as GPIO
import json
from random import randint
from evdev import InputDevice
from select import select

import SimpleMFRC522


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(13,GPIO.OUT)

class doorlock:

        global dbHost
        global dbName
        global dbUser
        global dbPass

        dbHost = 'localhost'
        dbName = 'mysql'
        dbUser = 'root'
        dbPass = 'raspberry'

        def __init__(self):
                try:
                        while 1:
                                self.listen_rfid()
                        #t.daemoon = True
                        #t.start()
                except KeyboardInterrupt:
			pass
        def returnToIdle_fromAccessGranted(self):
                GPIO.output(13,GPIO.LOW)


        def listen_rfid(self):
                reader = SimpleMFRC522.SimpleMFRC522()
                print("Please place your rfid")

                try:
                        id, text = reader.read()
                        dbConnection = MySQLdb.connect(host=dbHost, user=dbUser$
                        cur = dbConnection.cursor(MySQLdb.cursors.DictCursor)
                        cur.execute("SELECT * FROM access_list WHERE rfid_code $

                        if cur.rowcount !=1:
                                print("Access Denied")
                                cur.execute("INSERT INTO access_log SET Name = $
                                dbConnection.commit()

                                time.sleep(3)
                                self.returnToIdle_fromAccessGranted()
                        else:
                                cur.execute("INSERT INTO access_log SET Name = $
                                dbConnection.commit()
                                print("Access Granted, now an sms is sent")
                                GPIO.output(13,GPIO.HIGH)
                                dbConnection.close()
                                time.sleep(5)
                               self.returnToIdle_fromAccessGranted()
                finally:
                        GPIO.cleanup()


if __name__ == '__main__':
        w = doorlock()
        w.t.mainloop()

