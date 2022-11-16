from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import key2
from twilio.rest import Client

client = Client(key2.accountSID,key2.authToken)

twilionumber = '+13236121761'
myCellphone = '+18325256779'

url = 'https://coinmarketcap.com/'
# Request in case 404 Forbidden error
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}


req = Request(url,headers=headers)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage,'html.parser')

tr = soup.findAll('tr')

for row in tr[:6]:
    td = row.findAll('td')
    p = row.findAll('p')
    caret = row.findAll('span',class_='icon-Caret-up')
    if td:
        crypto_name = p[1].text
        crypto_symbol = p[2].text
        crypto_price = (td[3].text)
        crypto_change = (td[5].text)
        if caret:
            crypto_change = crypto_change
        else:
            crypto_change = '-' + crypto_change
        crypto_price_strip1 = crypto_price.replace('$','')
        crypto_price_strip2 = crypto_price_strip1.replace(',','')
        prev_price = round(float(crypto_price_strip2)/((float(crypto_change.rstrip(crypto_change[-1]))/100)+1),2)

        print(f'Name: {crypto_name}')
        print(f'Symbol: {crypto_symbol}')
        print(f'Price: {crypto_price}')
        print(f'% Change: {crypto_change}')
        print(f'Price prior to change: ${prev_price:,.2f}')
        print('')

        if p[1].text == "Bitcoin" and float(crypto_price_strip2)<40000:
            txtmsg = client.messages.create(to=myCellphone,from_=twilionumber,body="ALERT: Bitcoin's value has fallen below $40,000!")
        if p[1].text == "Ethereum" and float(crypto_price_strip2)<3000:
            txtmsg = client.messages.create(to=myCellphone,from_=twilionumber,body="ALERT: Ethereum's value has fallen below $3,000!")




