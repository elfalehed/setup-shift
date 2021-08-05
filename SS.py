#! /usr/bin/python3 
import os
import yaml

def installer(packages):
    i = 1
    for p in packages:
        print('[',i,']',p[0],'\n')
        i = i+1
    option = int(input(":$ "))
    # print(len(packages))
    if (option in range(0,len(packages)+1) ):
        os.system(packages[option-1][1])

def add():
    print("What's the name of the automated command: ")
    pack_name = str(input(':$ '))
    print("What's the command to run the command: ")
    pack_com = str(input(':$ '))
    pack = [pack_name,pack_com]
    return pack


def main():
    print("[1] Install packages \n[2] Add a package to the config\n")
    option = int(input(":$ "))
    with open('config.yaml','r') as file:
        config = yaml.safe_load(file)
        packages = config['packages']
    if (option == 1):
            installer(packages)
    elif (option == 2):
        with open('config.yaml','w') as file:
            config['packages'].append(add())
            yaml.dump(config,file)
            
if __name__=='__main__':main()
