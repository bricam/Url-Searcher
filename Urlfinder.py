import urllib
import re
import urllib.request
import requests
print('Functions available: tumblr(), tumblrloop(), twitter(), instagram()')
print('')
#####################Lists#####################
#Add string lists here



#####################Functions#####################
def checktwitter(url):
    r = requests.get("http://twitter.com/"+ url)
    if r.status_code == 404:
        return True

def checkinstagram(url):
    r = requests.get("http://instagram.com/"+ url)
    if r.status_code == 404:
        return True
    

def checktumblr(url):
    r = requests.get("http://"+ url + ".tumblr.com")
    if r.status_code == 404:
        return True
    
def tumblr(lst):
    print('Urls available:')
    for x in range(len(lst)):
        if checktumblr(lst[x]) == True:
            print(lst[x])
    print('************################Done################************')

def tumblrloop(lst):
    print('Urls available:')
    while(True):
        for x in range(len(lst)):
            if checktumblr(lst[x]) == True:
                print(lst[x])
    print('************################Done################************')


def twitter(lst):
    print('Urls available:')
    for x in range(len(lst)):
        if checktwitter(lst[x]) == True:
            print(lst[x])
    print('************################Done################************')

def instagram(lst):
    print('Urls available:')
    for x in range(len(lst)):
        if checkinstagram(lst[x]) == True:
            print(lst[x])
    print('************################Done################************')
