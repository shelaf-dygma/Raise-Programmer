#!/usr/bin/env python
import serial.tools.list_ports
import time, subprocess, serial, os

BOOTLOADER_VIDPID = '1209:2200'
RAISE_VIDPID = '1209:2201'

def reset_w_baud(baud=1200):
    ports = serial.tools.list_ports.grep(RAISE_VIDPID) # find the right port
    for port in ports:
        print("found %s port on %s" % (port.usb_description(), port.device))
        print("%d reset" % baud)
        serial.Serial(port=port.device, baudrate=baud)
        return True
    else:
        return False

def program_firmware():
    ports = serial.tools.list_ports.grep(BOOTLOADER_VIDPID) # find the right port
    for port in ports:
        print("found %s port on %s" % (port.usb_description(), port.device))
        print("programming firmware")
        os.system('bossac -i -d --port %s -e -o 0x2000 -w ./Raise-Firmware.ino.bin -R' % port.device)
        return True
    else:
        return False

# maybe already in bootloader mode
if program_firmware():
    exit(0)

# otherwise, prompt for user to press the special key
raw_input("when the Huble light goes out, press the 'esc' key. Press enter to continue")
if reset_w_baud():
    time.sleep(3)
    program_firmware()
else:
    print("couldn't find Dygma Raise")
