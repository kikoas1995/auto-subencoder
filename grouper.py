#!/usr/bin/python3
import sys
import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

if (len(sys.argv) < 2):
    print("Usage: ./grouper.py <shell.txt in \\xFF format>")
    exit()

readfile = sys.argv[1]

with open(os.path.splitext(readfile)[0] + '_grouped.txt', 'w') as outfile, open(readfile, 'r', encoding='utf-8') as infile: 
    shellcode = infile.read()
    print(bcolors.OKGREEN + "[+] Loaded shellcode is: " + bcolors.ENDC + shellcode)

    stripped_shellcode = shellcode.replace('\\x', '') 
    byteShellcode = bytearray.fromhex(stripped_shellcode)
    info = [byteShellcode[i:i+4] for i in range(0, len(byteShellcode), 4)]
    finalByteArray = bytearray()
    for subarray in reversed(info):
        if (len(subarray) < 4):
            subarray +=  bytearray(4 - len(subarray))
        
        finalByteArray += subarray[-1: -len(subarray)-1: -1]
    
    out = ''.join('%02x'%i for i in finalByteArray).upper()
    print(bcolors.OKGREEN + "[+] Grouped shellcode is: " + bcolors.ENDC + out)
    outfile.write(out + '\n')
