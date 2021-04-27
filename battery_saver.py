#!/usr/bin/python3
from psutil import sensors_battery # get battery info https://pypi.org/project/psutil/
from Arduino_Serial import Arduino_Serial
from time import strftime, localtime, sleep

# print message with timestamp
def printt(message):
    #timestamp = strftime("%y-%m-%d %H:%M GMT-7", localtime())
    timestamp = strftime("%y-%m-%d %H:%M:%S", localtime())
    print(f'{timestamp} | {message}')

# get battery data
def get_battery_data(): 
    battery = sensors_battery()
    return (battery.percent, battery.power_plugged) if battery is not None else (None, None)

# change relay state to charge/drain battery
def charge(option):
    # COM4 in Windows = /dev/ttyS4 in WSL
    arduino_port = 'COM4'
    # relay configured to be normally closed
    if option == 'on':
        printt('Plugging laptop in')
        with Arduino_Serial(arduino_port) as board:
            board.switch_on()
    if option == 'off':
        printt('Unplugging laptop')
        with Arduino_Serial(arduino_port) as board:
            board.switch_off()

# main control function
if __name__ == "__main__":
    turn_on = 40
    turn_off = 80
    state = 'charge'
    test_state = True
    sleep_minutes = 0.25
    while(True):
        percent, plugged = get_battery_data()
        if percent is None or plugged is None: # Demo states if no battery is present
            test_state = not test_state
            print(f"No battery installed. Performing Demo '{'on' if test_state else 'off'}' flip instead.")
            charge('on' if test_state else 'off')
        else: # Normal running states
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