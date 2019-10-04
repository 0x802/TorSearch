#!/usr/bin/env python3
import os
import sys
import time
try:
    import requests
except ImportError:
    print("[!!!] Error import 'requests' model ")
    exit()

try:
    from interruptingcow import timeout
except ImportError:
    print("[!!!] Error import 'interruptingcow' model ")
    exit()

try: 
    from bs4 import BeautifulSoup
except ImportError:
    print("[!!!] Error import 'bs4' model ")
    exit()

# COLORS
R = '\033[1;31m'
T = '\033[1;33m'
B = '\033[1;34m'
G = '\033[1;32m'
W = '\033[1;37m'
N = '\033[0m'

start = time.time()

proxies = {'http':'socks5h://127.0.0.1:9050', 'https':'socks5h://127.0.0.1:9050'} # tor proxy

def CHACK():
    try:
        requests.Session().get(url="http://127.0.0.1:9050")
        print(f"[ {T}+{N} ] Start Proxy Tor [ {G}ok{N} ]\n{'-'*50}\n")
    except requests.exceptions.ConnectionError as e:
        print(f"[ {T}+{N} ] Start Proxy Tor [ {R}NO{N} ]")
        print(f"[ {R}!{N} ] Pleas open tor proxy")
        exit()
        

def GET_TOR_LINKS(*args, **kwargs):
    try:
        with timeout(30):

            GET = requests.Session().get(url=f"http://msydqstlz2kzerdg.onion/search/?q={args[0]}", proxies=proxies).content

    except RuntimeError:
        print(f"[ {R}-{N} ] {W}Timeout{N} over")
        return None

    except requests.exceptions.ConnectionError:
        print(f"[ {R}-{N} ] No Proxy {W}Tor{N}")
        return None

    return GET

def GET_PROCESS_DATA(*args, **kwargs):
    print(f"{'-'*50}\n[ {B}*{N} ] Target : Dark web\n[ {B}*{N} ] Dorks  : {args[0].replace('+', ' ')}\n{'-'*50}\n")
    CHACK()
    GET = GET_TOR_LINKS(args[0])

    if GET != None:
        TO = BeautifulSoup(GET.decode(), "lxml")
        print(f"[ {T}+{N} ] Proxy tor [ {G}ok{N} ]")
        print(f"[ {T}+{N} ] Connection dark web [ {G}ok{N} ]")
        time.sleep(1)
        print(f"[ {T}+{N} ] Find {G}{len(TO.findAll('cite'))}{N} results in {time.time() - start} seconds\n{'-'*50}\n\n")
        [print(f"{T}Title:{N} {i.text.strip() if i.text.strip() != '' else R+'No Title'+N}\n{T}Url  : {N}{G}{j.text.strip() if len(j.text.strip()) <= 22 else R+'URL is False'+N}{N}\n{T}Date :{N} {d.text.strip()}\n{'-'*50}")\
                for i,j,d in zip(TO.findAll("h4"), TO.findAll("cite"),TO.findAll("span", {"class":"lastSeen"}))]
    else:exit()
    
if __name__ == "__main__":
    dork = str()
    try:
        s, *a = sys.argv
        if a == []:
            exit()
    except:
        print(f"Ex:\n\t\apython {s} <dork>")
        exit()

    if len(a) > 1:
        
        for i in a:dork += f'{i}+'

    else:dork = a[0]

    GET_PROCESS_DATA(dork)
