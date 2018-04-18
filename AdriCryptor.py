from sys import platform
import os
import subprocess
import requests
import gmpy2
from Crypto.Util.number import long_to_bytes

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

def clear():
    if platform == "win32":
        os.system('cls')
    else:
        os.system('clear')

def ceaser():
    print "Choose your Ceaser option:"
    print "1)Select chars"
    print "2)Alphatebetic chars"
    n = raw_input("Enter option: ")
    if n == "1":
        print "Enter your char list, exemple:\n !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
        alpha = raw_input("Enter your char list: ")
        cipher = raw_input("Enter your string: ")
        tamanho = len(alpha)
        for x in range(1, tamanho):        
            new_cipher = ""
            for letter in cipher:
                new_cipher+=alpha[(alpha.find(letter)+x) % len(alpha)]
            print new_cipher

    elif n == "2":
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
    else:
        clear()
        ceaser()
    exit(1)

def vignere():
    print "Choose your Vignere option:"
    print "1)encrypt"
    print "2)decrypt"
    mode = raw_input("Enter option: ")
    message = raw_input("Enter your message: ").lower()
    key = raw_input("Enter your key: ").lower()

    letters = "abcdefghijklmnopqrstuvwxyz"
    
    translated = ""
    keyIndex = 0
    
    for symbol in message:
        num = letters.find(symbol.lower())
        if num != -1:
            if mode == '1':
                num += letters.find(key[keyIndex])
            elif mode == '2':
                num -= letters.find(key[keyIndex])
    
            num %= len(letters)
    
            if symbol.isupper():
                translated+=letters[num]
            elif symbol.islower():
                translated+=letters[num]
    
            keyIndex += 1
            if keyIndex == len(key):
                keyIndex = 0
        else:
            translated+=symbol
    print "your message encrypted: " if mode == "1" else "your message decrypted: \n" + translated
    exit(1)

def transposition():
    exit(1)

def enigma():
    exit(1)

def rsa():
    print "What do you want to do?"
    print "1)decrypt"
    print "2)encrypt"
    print "3)factor N"
    know = raw_input("Enter option: ")
    if know == "1":
    	C = raw_input("Enter your ciphertext: ")
    	E = raw_input("Enter your expoent: ")
    	P = raw_input("Enter your first prime: ")
    	Q = raw_input("Enter your second prime: ")
    	N = P*Q
    	phi = (P - 1) * (Q - 1)
    	D = int(gmpy2.invert(E, phi))
    	M = pow(C, D, N)
    	print long_to_bytes(M)
    elif know == "2":
    	print "enc"
    elif know == "3":
    	number = raw_input("Enter your N number: ")
    	if(factordb(number)):
    		exit(1)
    	elif(neca(number)):
    		exit(1)
    	elif(yafu(number)):
    		exit(1)


def factordb(number):
    r = requests.get("https://factordb.com/index.php?query="+number, verify=False)
    vector = r.text.split("index.php?id=")
    if "middot" in vector[2]:
    	p = vector[2].split("\"")[0]
    	q = vector[3].split("\"")[0]
    	print "First prime: " + p
    	print "Second prime: " + q
    	return True
    else:
    	print "[+] factordb fail!"
    	return False

def neca(number):
	os.system("./neca/neca "+ number +" > neca_output")
	file = open("neca_output")
	linhas = file.readlines()
	if "Given key does not seem to be weak" in linhas[8]:
		print "[+] Neca fail!"
		return False
	else:
		print "Please, wait :)"
		numeros = linhas[-1].split(" * ")
		print "First prime: " + numeros[0][4:]
    	print "Second prime: " + numeros[1]

def yafu(number):
	os.system("echo \"factor("+number+")\" | wine ./YAFU/yafu-x64.exe")

def alphabetic_cipher():
    print "\nChoose the cipher!"
    print "a) Ceaser cipher"
    print "b) Vignere cipher"
    print "c) Transposition cipher"
    print "d) Enigma cipher\n"
    n = raw_input("Enter option: ")
    if n == "a":
        ceaser()
    elif n == "b":
        vignere()
    elif n == "c":
        transposition()
    elif n == "d":
        enigma()
    else:
        alphabetic_cipher()
def symmetric_cipher():
    print "Choose the cipher!"

def asymmetric_cipher():
    print "Choose the cipher!"
    print "a)RSA"
    n = raw_input("Enter option: ")
    if n == "a":
        rsa()
    else:
        asymmetric_cipher()

def main():
    clear()
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