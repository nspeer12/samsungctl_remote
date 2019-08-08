import socket
import subprocess
import samsungctl

def getIP():
	addr = input('Enter the IP Address of the Samsung TV: ')
	try:
		socket.inet_pton(socket.AF_INET, addr)
		return addr
	except socket.error:
		print('Invalid IP Address')
		return None

def checkOnline(ipAddr):
    res = subprocess.call(['ping', '-c', '3', ipAddr])
    return 1 if res == 0 else 0

def getRemote(config):
	remote = samsungctl.Remote(config)
	return remote
