#!/bin/sh

airmon-ng check kill
ifconfig $1 down
iwconfig $1 mode monitor
ifconfig $1 up
airodump-ng --band $2 --write drone $1 
