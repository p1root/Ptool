import sys
import os
def main():
    try:
        from colorama import Fore
    except:
        print("Please Install colorama\nyou can install colorama with this code ==> (pip install colorama)")
        sys.exit()

    try:
        import requests
    except:
        print(Fore.LIGHTRED_EX+"Please Install requests\n" +
            "you can install requests with this code ==> "+Fore.LIGHTBLUE_EX+" (pip install requests)")
        sys.exit()
    try:
        import ipapi
    except:
        print(Fore.LIGHTRED_EX+"Please Install ipapi\n" +
            "you can install ipapi with this code ==>"+Fore.LIGHTBLUE_EX+" (pip install ipapi)")
        sys.exit()

    from modules import IPfinder, PswGnt, admin, Banner
    os.system('cls')
    Banner.banner()
    while True:
        try:
            num = input("\n"+Fore.LIGHTBLACK_EX +
                        '  [Ptool] '+Fore.LIGHTGREEN_EX+"Enter a Number "+Fore.LIGHTBLUE_EX+":>> ")
            match num:
                case '1':
                    IPfinder.ipfinder()
                case '2':
                    PswGnt.password()
                case '3':
                    admin.admin()
                case '4':
                    break
                case '5':
                    break
                    
        except:
            print(Fore.RED+"Entered number is invalid ! "+Fore.LIGHTBLUE_EX)

if __name__ == '__main__':
    main()