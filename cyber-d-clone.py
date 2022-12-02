import os
from time import time
import time
os.system("pip install -r req.txt")


# logos
logo= """                                                                               
MMMMMMMM               MMMMMMMM                            DDDDDDDDDDDDD        
M:::::::M             M:::::::M                            D::::::::::::DDD     
M::::::::M           M::::::::M                            D:::::::::::::::DD   
M:::::::::M         M:::::::::M                            DDD:::::DDDDD:::::D  
M::::::::::M       M::::::::::Mrrrrr   rrrrrrrrr             D:::::D    D:::::D 
M:::::::::::M     M:::::::::::Mr::::rrr:::::::::r            D:::::D     D:::::D
M:::::::M::::M   M::::M:::::::Mr:::::::::::::::::r           D:::::D     D:::::D
M::::::M M::::M M::::M M::::::Mrr::::::rrrrr::::::r          D:::::D     D:::::D
M::::::M  M::::M::::M  M::::::M r:::::r     r:::::r          D:::::D     D:::::D
M::::::M   M:::::::M   M::::::M r:::::r     rrrrrrr          D:::::D     D:::::D
M::::::M    M:::::M    M::::::M r:::::r                      D:::::D     D:::::D
M::::::M     MMMMM     M::::::M r:::::r                      D:::::D    D:::::D 
M::::::M               M::::::M r:::::r                    DDD:::::DDDDD:::::D  
M::::::M               M::::::M r:::::r             ...... D:::::::::::::::DD   
M::::::M               M::::::M r:::::r             .::::. D::::::::::::DDD     
MMMMMMMM               MMMMMMMM rrrrrrr             ...... DDDDDDDDDDDDD                                                                                     
 """

social_media= """
 ~ Instagram: https://instagram.com/anand_ksri
 ~ Whatsapp: https://wa.me/+1(310)751-7352
 ~ Telegram: https://t.me/anand_ksri
"""

tool="""
|_______________ Installing _________________|
 ============================================
"""

success="""
|__________installation successful____________|
 =============================================
"""
can="""
|__________installation Cancelled____________|
 =============================================
"""
bye="""
 ▄▄▄▄ ▓██   ██▓▓█████ 
▓█████▄▒██  ██▒▓█   ▀ 
▒██▒ ▄██▒██ ██░▒███   
▒██░█▀  ░ ▐██▓░▒▓█  ▄ 
░▓█  ▀█▓░ ██▒▓░░▒████▒
░▒▓███▀▒ ██▒▒▒ ░░ ▒░ ░
▒░▒   ░▓██ ░▒░  ░ ░  ░
 ░    ░▒ ▒ ░░     ░   
 ░     ░ ░        ░  ░
      ░░ ░            
"""

from termcolor import colored
os.system("clear")
print(colored(logo,"blue") + colored(social_media,"red"))

install=input(colored("Do you want to install Cyber-D (y/n):","yellow"))
if install == "y":
    print(colored(tool,"green"))
    os.system("pkg update -y && pkg upgrade -y && pkg install python3")
    os.system("cd $HOME && rm -rf Cyber-D")
    os.system("cd $HOME && mkdir .tools")
    os.system("cd $HOME && git clone https://github.com/kdo2006/Cyber-D")
    os.system("cd $HOME && cd Cyber-D && cd fun && pip install -r fun/req.txt")
    print(colored(success,"green"))
    time.sleep(0.5)
    os.system("cd $HOME && cd Cyber-D && python3 CyberD.py")
elif install=="n":
    print(colored(can,"green"))
    time.sleep(0.5)
    print(colored(bye,"yellow"))
else:
    print(colored("[!] Invalid Option, Try Again...","red"))
    time.sleep(0.4)
    os.system("clear")
    os.system("python3 setup.py")