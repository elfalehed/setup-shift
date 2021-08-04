#! /usr/bin/python3 
import colorama
from colorama import Fore
import os

art = """
       .__     _____         .__           .__         .___                   
  ____  |  |  _/ ____\_____   |  |    ____  |  |__    __| _/  ____  ___  __  
_/ __ \ |  |  \   __\ \__  \  |  |  _/ __ \ |  |  \  / __ | _/ __ \ \  \/ / 
\  ___/ |  |__ |  |    / __ \_|  |__\  ___/ |   Y  \/ /_/ | \  ___/  \   / 
 \___  >|____/ |__|   (____  /|____/ \___  >|___|  /\____ |  \___  >  \_/  
     \/                    \/            \/      \/      \/      \/          """


def chrome():
    print(Fore.CYAN + ' [1] GitHunt')
    print(Fore.CYAN + ' [2] return to menu')

    print()
    option = int(input(":$ "))
    if(option == 1):
        os.system("google-chrome https://chrome.google.com/webstore/detail/githunt/khpcnaokfebphakjgdgpinmglconplhp?hl=en")
    elif(option == 2):
        setupinto()
        option = int(input(Fore.GREEN + ":$ "))
        setup(option)
def ides():
    print(Fore.CYAN + ' [1] VScode')
    print(Fore.CYAN + ' [2] SublimeText')
    print(Fore.CYAN + ' [3] Atom')
    print(Fore.CYAN + ' [4] return to menu')

    
    print()
    option = int(input(Fore.GREEN + ':$ '))
    if(option == 1):
        os.system("google-chrome https://code.visualstudio.com/docs/setup/linux")
    elif(option == 2):
        os.system("sudo apt-get install sublime-text")
    elif(option == 3):
        os.system("sudo apt-get install atom")
    elif(option == 4):
        setupinto()
        option = int(input(Fore.GREEN + ":$ "))
        setup(option)   


def webdev():
    print(Fore.CYAN + ' [0] npm')
    print(Fore.CYAN + ' [1] nodejs')
    print(Fore.CYAN + ' [2] materialui')
    print(Fore.CYAN + ' [3] tailwindcss')
    print(Fore.CYAN + ' [4] return to menu')

    print() 
    option = int(input(Fore.GREEN + ':$ ')) 
    if(option == 0): 
        os.system("sudo apt install npm")
    elif(option == 1):
        os.system("sudo apt install npm nodejs")
    elif(option == 2):
        os.system("npm install @material-ui/core")
    elif(option == 3):
        os.system("npm install -D tailwindcss@latest postcss@latest autoprefixer@latest")
    elif(option == 4):
        setupinto()
        option = int(input(Fore.GREEN + ":$ "))
        setup(option)   

def python():
    print(Fore.CYAN + ' [0] Update Python')
    print(Fore.CYAN + ' [1] Python GUI frameworks')
    print(Fore.CYAN + ' [2] Python Web frameworks')
    print(Fore.CYAN + ' [3] return to menu')

    print() 
    
    option = int(input(Fore.GREEN + ':$ ')) 
    
    if(option == 0): 
        os.system("sudo apt install python3.9")
    elif(option == 1):
        print(Fore.CYAN + ' [0] PyQt5')
        print(Fore.CYAN + ' [1] Kivy')
        print(Fore.CYAN + ' [2] wxPython')
        print(Fore.CYAN + ' [3] PySimpleGUI')
        
        option = int(input(Fore.GREEN + ':$ ')) 
        
        if(option == 0): 
            os.system("pip install PyQt5")
        elif(option == 1): 
            os.system("pip install Kivy")
        elif(option == 2): 
            os.system("pip install wxPython")    
        elif(option == 3): 
            os.system("pip install PySimpleGUI")
    
    elif(option == 2):
        print(Fore.CYAN + ' [0] Flask')
        print(Fore.CYAN + ' [1] Django')
 
        option = int(input(Fore.GREEN + ':$ ')) 
        
        if(option == 0): 
            os.system("pip install Flask")
        elif(option == 1): 
            os.system("pip install Django")
    elif(option == 3):
        setupinto()
        option = int(input(Fore.GREEN + ":$ "))
        setup(option)
               
    

def setupinto():
    print(Fore.YELLOW + ' [1] Web development packages and dependencies.')
    print(Fore.YELLOW + ' [2] Text Editors and IDEs') 
    print(Fore.YELLOW + ' [3] Chrome Extensions')
    print(Fore.YELLOW + ' [4] Python Tools')
    

    
def setup(option):
    if(option == 1):
        webdev()
    elif(option == 2): 
        ides()
    elif(option ==  3):
        chrome()
    elif(option ==  4):
        python()


def main():
    print(art)
    print(Fore.RED +' [!] You can change the download commands easily from the source-code.')
    print()
    setupinto()
    print()
    option = int(input(Fore.GREEN + ":$ "))
    setup(option)
    
if __name__=='__main__':main()
