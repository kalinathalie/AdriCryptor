from sys import platform
import os
import subprocess
def header():
	print "              _      _  _____                  _             "
	print "     /\      | |    (_)/ ____|                | |            "
	print "    /  \   __| |_ __ _| |     _ __ _   _ _ __ | |_ ___  _ __ "
	print "   / /\ \ / _` | '__| | |    | '__| | | | '_ \| __/ _ \| '__|"
	print "  / ____ \ (_| | |  | | |____| |  | |_| | |_) | || (_) | |   "
	print " /_/    \_\__,_|_|  |_|\_____|_|   \__, | .__/ \__\___/|_|   "
	print "                                    __/ | |                  "
	print "                                   |___/|_|                  "
	print "           AdriCryptor.py implemented by FireShell           "
	print "                   You're using:", platform

def ceaser():
	cipher = raw_input("Enter your string: ").lower()
	for x in range(1,26):
		new_cipher = ""
		for letter in cipher:
			if letter == " ":
				new_cipher += letter
				continue
			new_letter = (ord(letter)+x) % 123
			if new_letter < 97:
				new_letter+=97
			new_cipher += chr(new_letter)
		print new_cipher

def alphabetic_cipher():
	print "\nChoose the cipher!"
	print "a) Ceaser cipher"
	print "b) Vignere cipher"
	print "c) Transposition cipher"
	print "d) Enigma cipher"
	n = raw_input("Enter option: ")
	if n == "a":
		ceaser()
def symmetric_cipher():
	print "Choose the cipher!"

def asymmetric_cipher():
	print "Choose the cipher!"

def main():
	if platform == "win32":
		os.system('cls')
	else:
		os.system('clear')
	header()
	print "What do you wanna to decryt?"
	print "1) Polyalphabetic cipher"
	print "2) Symmetric cipher"
	print "3) Asymmetric cipher"
	print "4) Exit"
	n = raw_input("Enter option: ")
	if n == "1":
		alphabetic_cipher()
	elif n == "2":
		symmetric_cipher()
	elif n == "3":
		asymmetric_cipher()
	elif n == "4":
		exit(1)
	else:
		main()

if __name__ == '__main__':
	main()