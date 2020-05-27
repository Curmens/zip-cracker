
#!/usr/bin/python
# -*- coding: utf-8 -*-

# Importing Required modules

import time, optparse, zipfile, os
import pyzipper
from progress.bar import Bar


# "\033[38;5;2mHello World\033[0m"
banner = \
    '''\033[38;5;2                  
                            \033[1;31mCrack Zip File Password \033[1;33m
                    +--------------------------------------+   
                    |           Version : 1.0              |
	            |        ---------------------	   |
		    | Developed By : Pico_technology       |
		    | Author       : Curtis Mensah         |
                    | Instagram    : Pico_Technology       |  
                    | Website      : invalid               |  
                    | Github       : sitrucmensah          |
                    +--------------------------------------+  

-------OPTIONS-------
[1] Crack Zip File With CRC-32 encryption
[2] Info
[3] Exit Tool
 

\033[0m"
'''

print(banner)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# Main Function

def main():
    choice = input(f"{bcolors.OKGREEN}[+] Select an Option : {bcolors.ENDC}")


    if choice == '1':

    # Input path for zip file

        file_path = input('[+] Enter Zip File Path : ')
        file_path = file_path.replace(' ', '')

    # Input path for wordlist file
        word_list = input(f"{bcolors.OKGREEN}[+] Enter Wordlist Path : {bcolors.ENDC}") or './password.txt'
        word_list = word_list.replace(' ', '')
        z_file = zipfile.ZipFile(file_path)
        pwd_list = open(word_list)
        print (f"{bcolors.OKBLUE}[+] Brute Force Initiating ...{bcolors.ENDC}")
        time.sleep(3)
        print (f"{bcolors.OKBLUE}[+] Checking For Correct Password ...{bcolors.ENDC}")
        bar = Bar('Progress', max=1149945)
        for i in range(1149945):
            for line in pwd_list.readlines():
                passwd = line.strip('\n')
                # time.sleep(1)
                bar.next()
            
                # Password Brute Forcing
                try:
                    z_file.extractall(pwd=bytes(passwd, 'utf-8'))
                    print (f"{bcolors.OKBLUE}\n[+] Brute Force Completed! Password Found : '{passwd}'{bcolors.ENDC}")
                    if passwd != '':
                        break
                        print(f"{bcolors.FAIL}[+] Password Not Found in Given Wordlist {bcolors.ENDC}")
                except Exception:
                    pass
        bar.finish()
    elif choice == '2':
        print('\033[38;5;2mThis is a zip password crack tool for CRC-32 zip files only\nFor default password list hit the ENTER KEY\033[0m')
    elif choice == 3:
        print("Thank You !!")
        time.sleep(1)
        quit()
    else:
        print('Invalid option Try Again')
        main()


if __name__ == '__main__':
    main()
