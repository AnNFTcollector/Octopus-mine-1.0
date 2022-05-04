from telnetlib import theNULL
import time
import os
import sys
from zipapp import create_archive
import colorama
from termcolor import colored
from time import sleep
from os import system, name
from colorama import init, Fore, Back, Style
import platform
import psutil
import random
import string
import ctypes

ctypes.windll.kernel32.SetConsoleTitleW("Octopus mine - Operating - Pro version")

def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
clear()
print("")
print("")
print("")
print("")
print("")
print("")
print(colored("                               (------------)                                  ","green"))
print(colored("                               Gaining access.                                  ","blue"))
print("")
print("")
print("")
print("")
print("")
print("")
time.sleep(0.3)
clear()
print("")
print("")
print("")
print("")
print("")
print("")
print(colored("                               (====>-------)                                  ","green"))
print(colored("                               Access Gained...                                ","blue"))
print("")
print("")
print("")
print("")
print("")
print("")
time.sleep(0.3)
clear()
print("")
print("")
print("")
print("")
print("")
print("")
print(colored("                               (========>---)                                  ","green"))
print(colored("                            CHECKING FOR RESOURCES.                                  ","blue"))
print("")
print("")
print("")
print("")
print("")
print("")
time.sleep(0.3)
clear()
print("")
print("")
print("")
print("")
print("")
print("")
print(colored("                               (===========>)                                  ","green"))
print(colored("                              CHECKING SUCCESSFUL.                                  ","blue"))
print("")
print("")
print("")
print("")
print("")
print("")
clear()
print("")
time.sleep(0.03)
print("")
time.sleep(0.03) 
print(colored("             . ░█████╗░░█████╗░████████╗░█████╗░██████╗░██╗░░░██╗░██████╗  ███╗░░░███╗██╗███╗░░██╗███████╗","white"))
time.sleep(0.03)
print(colored("             . ██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██║░░░██║██╔════╝  ████╗░████║██║████╗░██║██╔════╝","white"))
time.sleep(0.03)
print(colored("             . ██║░░██║██║░░╚═╝░░░██║░░░██║░░██║██████╔╝██║░░░██║╚█████╗░  ██╔████╔██║██║██╔██╗██║█████╗░░","white"))
time.sleep(0.03)
print(colored("             . ██║░░██║██║░░██╗░░░██║░░░██║░░██║██╔═══╝░██║░░░██║░╚═══██╗  ██║╚██╔╝██║██║██║╚████║██╔══╝░","white"))
time.sleep(0.03)
print(colored("             . ██║░░██║██║░░██╗░░░██║░░░██║░░██║██╔═══╝░██║░░░██║░╚═══██╗  ██║╚██╔╝██║██║██║╚████║██╔══╝░","white"))
time.sleep(0.03)
print(colored("             . ╚█████╔╝╚█████╔╝░░░██║░░░╚█████╔╝██║░░░░░╚██████╔╝██████╔╝  ██║░╚═╝░██║██║██║░╚███║███████╗","white"))
time.sleep(0.03)
print(colored("             . ░╚════╝░░╚════╝░░░░╚═╝░░░░╚════╝░╚═╝░░░░░░╚═════╝░╚═════╝░  ╚═╝░░░░░╚═╝╚═╝╚═╝░░╚══╝╚══════╝","white"))
time.sleep(0.03)
print("")
time.sleep(0.03)
print("")


welcome = Fore.BLUE + "Coccecting to the server...\n"
for char in welcome:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.03)

time.sleep(0.5)

threads = Fore.GREEN + ">>> " + Fore.BLUE + "Connected...     Checking for server status... Server status:\n"
for char in threads:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.03)

time.sleep(1.3)
print(Fore.LIGHTMAGENTA_EX + "")

server = Fore.GREEN + ">>> " + Fore.GREEN + "Server operating...\n"
for char in server:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.03)

time.sleep(1.3)
print(Fore.WHITE + "Premium version")
time.sleep(1.0)
print(Fore.WHITE + "User approved")
time.sleep(0.5)
print(Fore.WHITE + "Connecting to the host...")
time.sleep(0.5)
print(Fore.WHITE + "Connected.")
time.sleep(1.3)
print(Fore.WHITE + "1%")
time.sleep(1.0)
print(Fore.WHITE + "28%")
time.sleep(0.5)
print(Fore.WHITE + "67%")
time.sleep(0.5)
print(Fore.WHITE + "100%")

start = Fore.GREEN + ">>> " + Fore.BLUE + " OCTOPUS MINE \n"
for char in start:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.2)



time.sleep(0.5)
print(Fore.RED + "Launching miner.")
time.sleep(1.5)

print("")
print("")

ctypes.windll.kernel32.SetConsoleTitleW("OCTOPUS MINE - - Currently operating - - Mining - - premium version- -")

def get_random_string(length):
    letters = string.ascii_uppercase + string.digits
    result_str = ''.join(random.choice(letters) for i in range(length))
    print(Fore.WHITE + "-" + Fore.BLUE + "OCTOPUSMINE" + Fore.WHITE + "-" + "  Wallet: " + Fore.RED + result_str + Fore.WHITE + "  /" + "RESULT: " + Fore.BLUE + "0.00000 BTC - - Wallet status: (Locked / Empty)" + Fore.WHITE + "/")

for i in range(1000):
    get_random_string(35)
    time.sleep(0.00000001)
    


def get_random_win(length):
    letters = string.ascii_uppercase + string.digits
    result_str = ''.join(random.choice(letters) for i in range(length))
    print(Fore.WHITE + "-" + Fore.GREEN + "OCTOPUSMINE" + Fore.WHITE + "-" + "  Wallet:: " + Fore.LIGHTGREEN_EX + result_str + Fore.WHITE + "  /" + "Amound: " + Fore.GREEN + "0.00423 BTC" + Fore.WHITE + "/")

time.sleep(0.3)

get_random_win(35)

time.sleep(0.5)

ctypes.windll.kernel32.SetConsoleTitleW("OCTOPUS MINE - 0.00423 BTC found! --Found:0.00423--")

print("")
print("")
time.sleep(1)
print(Fore.WHITE + "[" + Fore.GREEN + "OCTOPUS MINE" + Fore.WHITE + "]" + Fore.LIGHTGREEN_EX + " SAVING '0.00423 BTC' TO WALLET.TXT" + Fore.WHITE + "  [" + "RESULT: " + Fore.GREEN + "APPROVED" + Fore.WHITE + "]") 
time.sleep(1)
print("")
time.sleep(1)
print(Fore.RED + "BTC Sent to wallet" )

	
answer = input("Do you want to continue? yes or no: ") 
if answer == "yes": 

   def get_random_string(length):
       letters = string.ascii_uppercase + string.digits
       result_str = ''.join(random.choice(letters) for i in range(length))
       print(Fore.WHITE + "[" + Fore.BLUE + "OCTOPUSMINE" + Fore.WHITE + "]" + "  TESTING WALLET: " + Fore.RED + result_str + Fore.WHITE + "  [" + "RESULT: " + Fore.BLUE + "0.00 BTC" + Fore.WHITE + "]")

   for i in range(100000000000):
       get_random_string(35)
       time.sleep(0.000000000000000001)

elif answer == "no": 
    
  start = Fore.GREEN + ">>> " + Fore.BLUE + " 'Quiting aplication... \n"
  for char in start:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.2)
    
    quit()
else: 
    print("Please enter yes or no.") 


