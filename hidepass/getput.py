#!/usr/bin/python3
import termios 
import tty
import sys

def getchar():
	fd = sys.stdin.fileno()
	old_settings = termios.tcgetattr(fd)
		
	try:	
		tty.setraw( sys.stdin.fileno() )
		key = sys.stdin.read(1)
		
	finally:
		termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
		
	return key

def putchar(char):
	sys.stdout.write(char)
	sys.stdout.flush()
