#
# importlib pygame
# import datetime from datetime
# class AlarmClock:
#     def __init__(self):
#         alarm_time = None
#     def set_alarm(self):
#         set_alarm = {hour}: {minute}
#         print(f“Alarm set for {hour}:{minute}”)
#
#     def check_alarm(self):

from time import strftime
from tkinter import *

import time
import datetime
from pygame import mixer

class AlarmClock:
    def __init__(self):
        alarm_time = None


    def set_alarm(self):
    alarm_time = {hrs.get()}:{mins.get()}}
    print(alarm_time)
    print(f“Alarm set for{hour}: {minute}”)


def check_alarm(alarm_time):
    while True:
        time.sleep(1)
        time_now = datetime.datetime.now().strftime("%H:%S")

        current_time = time.localtime(time.time()) print(time_now)
        if time_now == alarmtime:
            Wakeup = Label(root, font=('arial', 20, 'bold'),
                           text="Wake up!Wake up!Wake up", bg="DodgerBlue2", fg="white").grid(row=6, columnspan=3)
            print("Alarm! It’s time to wake up!”!")
            mixer.init()
            mixer.music.load(rC:\Users\Bogdan\PycharmProjects\pythonProject\PYTHONPROJECTS\proiecte_python\Alarm-Clock-with-Python-main\Alarm-clock-ringing-sound-effect\Alarm-clock-ringing-sound-effect.mp3:)
            mixer.music.play()
            break

