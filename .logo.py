from os import system

try:
        import pyfiglet
except:
        system("pip install pyfiglet")

import pyfiglet

B='\033[1;36m'
Ra="\033[;31m"
R="\033[;39m"
G="\033[1;92m"
print("*"*75)
logo= pyfiglet.figlet_format('INSTALL_NGROK')
print(B+logo+R)
print(f"{R}[{G} ☆ {R}] {Ra}CH {G}@abnhay {B}&&{R} [{G} ☆ {R} ] {Ra}BY {G}@knk_1k{R}")
print("")
print("*"*75)