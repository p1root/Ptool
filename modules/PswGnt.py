import os
import time
import random
import subprocess
import platform
from colorama import Fore
from PTool import main


def password():
    chars = ['abcdefghijklmnopqrstuvwxyz'
            'ABCDEFGHIJKLMNOPQRSTUVWXYZ', '@#$%&*_', '1234567890']

    # -------------------CREAT_PASSWORD---------------------------------

    password = ''
    i = 0
    while i < 8:
        psd = random.choice(chars)

        password = str(password) + str(random.choice(psd))
        i = i + 1

    # -------------------------COPY_PASSWORD--------------------------

    if platform.uname()[0] == 'Windows':
        os.system('cls')
        copy = subprocess.getoutput(f'powershell.exe set-clipboard {password}')
        time.sleep(2)
                
    # -----------------------PRINT_PASSWORD--------------------------    
    
        os.system('cls')
        print('\n'+Fore.LIGHTBLACK_EX+'  [Ptool] '+Fore.LIGHTCYAN_EX +
              '  Your Password is: '+Fore.LIGHTBLUE_EX+password)
        # print('\n'+Fore.LIGHTRED_EX+'  Password Copied to Cilpboard!!')
    else:
        print('\n'+password)
        
    # -------------------------EXIT--------------------------
    try:
        input('\n'+Fore.GREEN + "   [*] Back To Menu (Press Enter...) ")
    except:
        main()
