# Raise programmer

This programmer is for Linux command line.

## About

The Huble contains a SAMD Arm 21 chip from Atmel. This can be programmed with the bossa programmer once
the chip is in 'bootloader mode'.

For security reasons, it can only be put in bootloader mode with your help:

* double pressing the reset button.
* pressing the escape or delete key after a software controlled reset.

This programmer will attempt to find a plugged in Huble, reset it via serial and then program the new firmware.

## Install requirements

Install a new version of bossac. You may need to apt-get install libwxgtk3.0-dev

    git clone https://github.com/shumatech/BOSSA
    cd BOSSA
    make
    sudo cp bin/bossac /usr/local/bin

Install pyserial

    sudo pip install pyserial

## Get new firmware

Put the new firmware in this directory, and make sure it's called Raise-Firmware.ino.bin

## Program the firmware

Run the programmer and follow the instructions. You will be promtpted to press the Escape key:

    ./program.py
