#!/bin/python2.7
# coding=utf-8

#
# https://github.com/arduino/_arduino/blob/ide-1.5.x/build/shared/manpage.adoc
#

import subprocess
import sys
import os.path
import re

# TODO add exception
#   - user not in group tty… to upload to the board (_linux)
#   - arduino UI not install


class UploadArduino:

    def __init__(self):
        self.__arduino_type = {}

        # TODO link every board name to package:arch:board
        # https://github.com/arduino/_arduino/blob/ide-1.5.x/build/shared/manpage.adoc

        self.__arduino_type["uno"] = "arduino:avr:uno"

        pass

    def __arduino_ui_is_install_linux(self):
        return os.path.isfile("/usr/bin/arduino")

    def __arduino_ui_is_install_windows(self):
        pass

    def __get_arduino_arch_board(self, arduino_type):
        arduino_type = arduino_type.lower()

        for key in self.__arduino_type:
            arduino_arch = re.search(key, arduino_type)
            if arduino_arch:
                return self.__arduino_type[key]

        return ""

    def __upload_linux(self, arduino_type, serial_port, arduinofile):
        if not self.__arduino_ui_is_install_linux():
            print "_error, Arduino UI is not install on your machine"
            sys.exit(1)

        arduino_arch = self.__get_arduino_arch_board(arduino_type)

        if arduino_arch == "":
            print "_error, the Arduino board architecture is unknown"
            sys.exit(1)

        #
        # TODO manage sudo error:
        # can't open device "/dev/...": no such file or directory
        #

        # arduino --board arduino:avr:uno --port /dev/tty_aCM0
        # --upload /home/battosai/_arduino/buzzer/buzzer.ino
        command = ['arduino', '--board', arduino_arch, '--port',
                   serial_port, '--upload', arduinofile]

        proc = subprocess.Popen(command, stdout=subprocess.PIPE)
        proc_stdout = proc.stdout.read()

        print proc_stdout

    def __upload_windows(self, arduino_type, serial_port, arduinofile):
        pass

    def upload(self, arduino_type, serial_port, arduinofile):

        print arduino_type, serial_port, arduinofile

        if sys.platform.startswith('linux'):
            print "_linux"
            return self.__upload_linux(arduino_type, serial_port, arduinofile)

        elif sys.platform.startswith('win'):
            print "_windows"
            return self.__upload_windows(arduino_type, serial_port, arduinofile)

if __name__ == '__main__':
    upload_arduino = UploadArduino()
    upload_arduino.upload("uno", "/dev/tty_aCM0", "/home/battosai/_arduino/buzzer/buzzer.ino")
