import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
import wget
import requests
import pyfiglet
import tweepy
import os
from PIL import Image

def main():
    url = 'https://www.reddit.com/r/wallpapers'
    #as u can see in url u have the r/wallpapers page
    
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    headers = {'User-Agent': user_agent}
    response = requests.get(url,headers=headers)
    html = response.content
    bs = BeautifulSoup(html, 'html.parser')
    
    y = 'https://www.reddit.com/r/wallpapers/comments'
    print('Getting Wallpapers...')
    
    for i in bs.find_all('a'):
        bruh = i.get('href')
        #since 'bruh' gets us a lot of links that do no referr to posts, i made this condition control to see if the variable Y
        #which is the standard starting link of any post is included in any of the links that bruh gets us
        #means we will get rid of useless links
        
        if (y in bruh ):
        #the the subUrl function is called if so
            subUrl(bruh)

    

def otherWebSite():
    sub_url = "https://www.pexels.com/search/wallpaper/"
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    headers = {'User-Agent': user_agent}
    response = requests.get(sub_url,headers=headers)
    html = response.content
    bs = BeautifulSoup(html, 'html.parser')
    y = 'https://images.pexels.com/photos/'
    x=0
    for tag in bs.find_all('img'):
        bruh = tag.get('src')
        if ( y in bruh ):
            bruh = bruh.replace("1&w=500","3&h=750&w=1260",1)
            bruh = bruh.replace("1&w=400","3&h=750&w=1260",1)
            print('Downloading image  ')
            response = requests.get(bruh,headers=headers)
            html = response.content
            with open(str(x) + '.jpg', 'wb') as f:
                f.write(html)
                f.close()
                x += 1

def subUrl(sub_url):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    headers = {'User-Agent': user_agent}
    response = requests.get(sub_url,headers=headers)
    html = response.content
    bs = BeautifulSoup(html, 'html.parser')
    y = 'https://i.redd.it'
    #same concept as main but y variable changes
    #and url takes links from 'bruh'

    for tag in bs.find_all('a'):

        bruh = tag.get('href')
        if ( y in bruh ):
        #also same concept as the previous control one
            print('Downloading image  ')
            filename = wget.download(bruh)
        #this downloads the picture
            print('\n Success! '+filename+' was downloaded on your computer')
            break
        #the break doesnt allow duplicates
             
def reName():
    i = 0
    for fileName in os.listdir('.'): 
        dst = str(i) + ".jpg"
        if (".py" in fileName)or(os.path.exists(dst)):
            pass
        else:
            os.rename(fileName, dst)
            print(fileName+" has been renamed to "+dst+" !")   
        i += 1
    
def reRes():
    i = 0
    for fileName in os.listdir('.'): 
        dst = str(i) + ".jpg"
        if (".py" in fileName):
            pass
        else:
            im = Image.open(dst)
            im.save(dst, dpi=(600,600))
            print(dst+" resolution has been changed!")
        i += 1
        
    
def share():
    auth = tweepy.OAuthHandler("", "")
    auth.set_access_token("","")
    api = tweepy.API(auth)
    
    for i in range(100):
        dst = str(i)+".jpg"
        try:
          api.update_with_media(dst)
          print(dst+" has been shared!")
          os.remove(dst)
        except:    
          pass
    

def lastMessage():
	print('\n')
	print('*****Thanks for using Pyper*****'+'\n')
	print('--------------------------------------'+'\n')
	input('*****press enter to exit**************'+'\n')


main()
#otherWebSite()
reName()
reRes()
share()
lastMessage()

