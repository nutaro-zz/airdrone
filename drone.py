import os, uuid

from subprocess import run


if os.geteuid() != 0:
    print("We must be root")
    raise PermissionError

log_file = open(f"/var/log/airdrone-{uuid.uuid4()}", 'w+') 
interface = input("Enter the wireless interface: ")

commands = [["airmon-ng", "check", "kill"],
            ["ifconfig", interface, "down"],
            ["iwconfig", interface, "mode", "monitor"],
            ["ifconfig", interface, "up"],
            [f"""airodump-ng --band abg --write drone {interface}"""]]

for command in commands:
    print(command)
    run(command, shell=True, check=True, stderr=log_file)

log_file.close()