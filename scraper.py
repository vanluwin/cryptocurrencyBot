from bs4 import BeautifulSoup
import smtplib as mail
import requests as req
from time import sleep

def sendMail(currencys):
    # Start a conection with gmail 
    server = mail.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('email', 'passwd')

    body = 'Dear user,\n\nCheck the price of the top 10 cryptocurrencys\n\n'
    for currency in currencys:
        body += '\n'.join(': '.join((str(k),str(v))) for k,v in currency.items()) + '\n\n'
    body += 'Best regards,\nBoberto'

    msg = f'Subject: Cryptocurrency Prices\n\n{body}'

    server.sendmail(
        'from',
        'to',
        msg
    )
    
    server.quit()

def checkPrices():

    URL = 'https://www.coinbase.com/price'

    # Google for my user agent
    headers = {
        'User-Agent': ''
    }

    page = req.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    rawTable = soup.find_all(attrs='AssetTableRow__Wrapper-sc-1e35vph-0 dsdazY', limit=10)

    currencys = []
    for row in rawTable:
        row = row.get_text('|').split('|')
        currencys.append({
            'Coin': row[1],
            'Price': row[3],
            'Change': row[4] + row[5],
            'Market Cap': row[6]
        })

    sendMail(currencys)

if __name__ == '__main__':
    # Checks prices daily
    while(True):
        checkPrices()
        sleep(86400)
