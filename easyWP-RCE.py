#!/usr/bin/env python3
# Author: Moad Akhraz @mdakh404 - twitter.com/mdakh404


import argparse
import requests
from bs4 import BeautifulSoup
from termcolor import colored



def get_args():
    parser = argparse.ArgumentParser(epilog='./easyWP-RCE.py target-wp.com')
    parser.add_argument('target' , help='Target wordpress-based site')
    return parser.parse_args()

args = get_args()

if ('http://' or 'https://') not in args.target:
    args.target = 'http://' + args.target

def main():

    banner = """
                                                                                                         
                     _ _ _ _____     _____ _____ _____ 
     ___ ___ ___ _ _| | | |  _  |___| __  |     |   __|
    | -_| .'|_ -| | | | | |   __|___|    -|   --|   __|
    |___|__,|___|_  |_____|__|      |__|__|_____|_____|
                |___|                                  
                       @mdakh404 - twitter.com/mdakh404               

"""

    print(colored(banner, 'red', attrs=['bold']))
    
    try:    

        req = requests.get(f'{args.target}/wp-admin/install.php')
        if req.status_code == 200:
            print(colored('\n[+] Target file is found ! Proccessing it ...', 'green', attrs=['bold']))
            soup = BeautifulSoup(req.text, 'html.parse')
            if 'WordPress' not in soup.title.get_text():
                print(colored(f"[-] Error: {args.target} isn't a WordPress site !", 'red', attrs=['bold']))
            
            heading = soup.find_all('h1')
            if heading[0].get_text() == 'Already Installed':
                print(colored('[-] Already Installed :(', 'red', attrs=['bold']))
            
            else:
                print(colored('[+] Maybe There is an install option, go and get it :)', 'red', attrs=['bold']))


        elif req.status_code == 404:
            print(colored('\n[-] Error: Target file is not found on the server !', 'red', attrs=['bold'])) 

        else:
            print(colored('\n[-] Error: The Server may not authorize us to access the file !', 'red', attrs=['bold']))
    
    except KeyboardInterrupt:
         print('\n[-] Exit ...')
         exit()
         
    except:
         print('\n[-] Error: Unkown error has been occured, check your connection/argument.')
    


if __name__ == '__main__':
    main()