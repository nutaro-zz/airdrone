import os, uuid
import click

from subprocess import run


@click.command()
@click.option('--interface', prompt="wireless card")
def get_packages(interface):

    if os.geteuid() != 0:
        print("We must be root")
        raise PermissionError

    log_file = open(f"/var/log/airdrone-{uuid.uuid4()}", 'w+') 

    commands = [["airmon-ng", "check", "kill"],
                ["ifconfig", interface, "down"],
                ["iwconfig", interface, "mode", "monitor"],
                ["ifconfig", interface, "up"],
                [f"""airodump-ng --band abg --write drone {interface}"""]]

    for command in commands:
        print(command)
        run(command, shell=True, check=True, stderr=log_file)

    log_file.close()


if __name__ == "__main__":
    