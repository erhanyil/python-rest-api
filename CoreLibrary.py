from colorama import Fore, Back, Style, init
import time, importlib
import json

class CoreLibrary:

    version = '0.0.1'
    
    def get_info(self):
        print(Back.MAGENTA)
        print("Current version: " + self.version)
        print (Style.RESET_ALL)

    def __init__(self):
        init()

    def returnValue(self, data): 
            return json.dumps(data)

    def consoleLog(self, message, info='info'):
        if(info == 'info'):
            print(Back.GREEN + Fore.LIGHTCYAN_EX + time.strftime("%c") + Fore.WHITE  + " Info: " + message + Style.RESET_ALL)
        else:
            print(Back.RED + Fore.LIGHTCYAN_EX + time.strftime("%c") + Fore.WHITE + " Error: " + message + Style.RESET_ALL)