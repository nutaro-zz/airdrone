import os

from subprocess import Popen

if os.geteuid() != 0:
    print("We must be root")
    raise PermissionError

interface = input("Enter the wireless interface: ")

Popen(["airmon-ng", "check", "kill"])

Popen(["ifconfig", interface, "down"])
Popen(["iwconfig", interface, "mode", "monitor"])
Popen(["ifconfig", interface, "up"])

Popen(["airodump-ng", "--band", "abg", interface])