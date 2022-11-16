import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request


random_chapter = str(random.randint(1,21))
print(random_chapter)
webpage = 'https://biblehub.com/asv/john/' + random_chapter + '.htm'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(webpage, headers=headers)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage,'html.parser')

verses = soup.findAll("p",class_='reg')
#print(verses)
verse_list = []

for verse in verses:
    verse_list = verse.text.split('.')
print(verse_list)
myverse = 'Chapter: ' + random_chapter + ' Verse: ' + random.choice(verse_list)
print(myverse)


import key2
from twilio.rest import Client

client = Client(key2.accountSID,key2.authToken)

twilionumber = '+13236121761'
myCellphone = '+18325256779'

textmsg = client.messages.create(to=myCellphone,from_=twilionumber,body = myverse)
