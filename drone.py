import os, uuid

from subprocess import call


if os.geteuid() != 0:
    print("We must be root")
    raise PermissionError

log_file = open(f"/var/log/airdrone-{uuid.uuid4()}", 'w+') 
interface = input("Enter the wireless interface: ")

commands = [["sudo", "-s", "airmon-ng", "check", "kill"],
            ["sudo", "-s", "ifconfig", interface, "down"],
            ["sudo", "-s", "iwconfig", interface, "mode", "monitor"],
            ["sudo", "-s", "ifconfig", interface, "up"],
            ["sudo", "-s","airodump-ng", "--band", "abg", interface]]

for command in commands:
    print(command)
    call(command, shell=True, stdout=log_file, stderr=log_file)

log_file.close()