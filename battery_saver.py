#!/usr/bin/python3
from psutil import sensors_battery # get battery info https://pypi.org/project/psutil/
from time import strftime, localtime, sleep
from requests import post

# get webhook secret from file and setup webhook
with open('webhook.txt', 'r') as file:
    url = ['https://maker.ifttt.com/trigger/', f'/json/with/key/{file.read().strip()}']

# print message with timestamp
def printt(message):
    timestamp = strftime("%y-%m-%d %H:%M:%S", localtime())
    print(f'{timestamp} | {message}')

# get battery data
def get_battery_data(): 
    battery = sensors_battery()
    return (battery.percent, battery.power_plugged) if battery is not None else (None, None)

# change outlet charge/drain battery
def charge(target):
    if target == 'on':
        printt('Plugging laptop in')
        post(f'{url[0]}charge{url[1]}')
    if target == 'off':
        printt('Unplugging laptop')
        post(f'{url[0]}charge{url[1]}')

# main control function
if __name__ == "__main__":
    turn_on = 40
    turn_off = 80
    state = 'charge'
    sleep_minutes = 3
    while(True):
        percent, plugged = get_battery_data()
        printt(f'{percent}% and {"Plugged In" if plugged else "Not Plugged In"}')
        # looping states
        if state == 'charge' and percent >= turn_off:
            charge('off')
            state = 'drain'
        elif state == 'drain' and percent <= turn_on:
            charge('on')
            state = 'charge'
        # redundancy
        elif state == 'charge' and not plugged:
            charge('on')
        elif state == 'drain' and plugged:
            charge('off')
        sleep(60 * sleep_minutes)