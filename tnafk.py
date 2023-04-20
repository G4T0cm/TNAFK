import random
import string
import urllib.parse

yellow='\033[93m'
gren='\033[92m'
cyan='\033[96m'
pink='\033[95m'
red='\033[91m'
b='\033[1m'

def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk)) 
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))
prGreen("""\
_____ _   _   ___  ______ _   __
|_   _| \ | | / _ \ |  ___| | / /
  | | |  \| |/ /_\ \| |_  | |/ / 
  | | | . ` ||  _  ||  _| |    \ 
  | | | |\  || | | || |   | |\  \\
  \_/ \_| \_/\_| |_/\_|   \_| \_/
                    """)
prRed("--Tottaly Not A Fake Domain --")
prYellow("--Created by G4T0--")
print (" ")
prRed("Dont add .com or similar extensions")

def generate_evil_domain(domain_to_spoof):
    ascii_domain = domain_to_spoof.encode('ascii')
    punycode_domain = urllib.parse.quote(ascii_domain).replace('%', '\\u00')
    if 'a' in punycode_domain:
        spoofed_domain = punycode_domain.replace('a', 'а', 1)
    else:
        spoofed_domain = punycode_domain.replace(punycode_domain[1], 'а', 1)
    return spoofed_domain

domain_to_spoof = input("Enter domain to spoof: ")
spoofed_domain = generate_evil_domain(domain_to_spoof)

print(f"Your spoofed domain is: {spoofed_domain}.com")
