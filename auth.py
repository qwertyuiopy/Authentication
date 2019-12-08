import requests
from colorama import Fore, init
init()

pasteLink = ''#input('Enter RAW Pastebin URL: ')

Users = []

with open('users.txt', 'r') as f:
    for line in f:
        for user in line.split():
            Users.append(user)

def Auth():
    r = requests.get(pasteLink)
    for i in r.content.decode('utf-8').split():
        if i in Users:
            print('['+Fore.GREEN+'+'+Fore.WHITE+']'+' Authenticated User {}'.format(i))
        else:
            print('['+Fore.RED+'-'+Fore.WHITE+']'+' Failed To Authenticate User')

if __name__ == '__main__':
    Auth()