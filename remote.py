import sys
import samsungctl
from networkConfigSamsung import *

def main():
	print('Welcome to Samsung Smart TV Remote')

	# get input and check for valid ip
	ipAddr = None

	if len(sys.argv) > 1:
		ipAddr = sys.argv[1]
	else:
		while(ipAddr == None):
			ipAddr = getIP()


	if checkOnline(ipAddr) == 1:
		print('Device is online')
	else:
		print('Error! Device is offline. Check connection and try again')
		return

	# need to make cleaner later
	config = {
    "name": "samsungctl",
    "description": "PC",
    "id": "",
    "host": ipAddr,
    "port": 55000,
    "method": "legacy",
    "timeout": 0,
	}

	remote = getRemote(config)
	remoteOn = 1

	print('Welcome to the Samsung TV Remote')
	while(remoteOn):
		menu(remote)

def menu(remote):
	print('UP: w')
	print('DOWN: s')
	print('LEFT: a')
	print('RIGHT: d')
	print('Volume Up: e')
	print('Volume Down: q')

	sequence = input('enter one or more keys: ')

	for x in sequence:
		remote.control(getKeyCode(x))

	return

def getKeyCode(ch):
	if ch == 'w':
		return 'KEY_UP'
	elif ch == 'a':
		return 'KEY_LEFT'
	elif ch == 's':
		return 'KEY_DOWN'
	elif ch == 'd':
		return 'KEY_RIGHT'
	elif ch == 'q':
		return 'KEY_VOLDOWN'
	elif ch == 'e':
		return 'KEY_VOLUP'


main()
