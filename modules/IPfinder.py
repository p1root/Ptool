import ipapi
from colorama import Fore
import time
import sys
import os

from PTool import main



def ipfinder():

    # Get IP From User --------------------------------
    os.system('cls')
    try:
        url = input('\n'+Fore.LIGHTBLACK_EX +
                    '  [Ptool] '+Fore.LIGHTGREEN_EX+'Enter IP or URL'+Fore.LIGHTBLUE_EX+' :>> ').title()
        target = ipapi.location(ip=url, key=None, options=None)

    # print result --------------------------------
        os.system("cls")
        print()
        print('\n'+Fore.LIGHTBLACK_EX +
              '  [Ptool] '+Fore.LIGHTRED_EX+' IP: >> ' + Fore.LIGHTBLUE_EX + target['ip'])
        time.sleep(.500)
        print('\n'+Fore.LIGHTBLACK_EX+'  [Ptool] '+Fore.LIGHTRED_EX +
              ' City : >> ' + Fore.LIGHTBLUE_EX + target['city'])
        time.sleep(.500)
        print('\n'+Fore.LIGHTBLACK_EX+'  [Ptool] '+Fore.LIGHTRED_EX +
              ' Regin : >> ' + Fore.LIGHTBLUE_EX + target['region'])
        time.sleep(.500)
        print('\n'+Fore.LIGHTBLACK_EX+'  [Ptool] ' + Fore.LIGHTRED_EX +
              ' Country : >> ' + Fore.LIGHTBLUE_EX + target['country_name'])
    except:
        print('\n'+Fore.LIGHTBLACK_EX+'  [Ptool] '+Fore.RED+'Eroor !!')
        time.sleep(2)
        main()
    # ------------------------------------------------

    try:
        print("")
        input(Fore.GREEN + " [*] Back To Menu (Press Enter...) ")
    except:
        main()
