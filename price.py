import requests
from bs4 import BeautifulSoup
import smtplib
import time


URL = ("https://www.buscape.com.br/fone-de-ouvido-e-headset/fone-de-ouvido-bluetooth-com-microfone-apple-airpods-2-estojo-sem-fio?_lc=88&q=airpods%20apple")
browser = {"user-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"}
WANTED_PRICE = 1000

def trackPrice():
    price = int(getPrice()[2].replace(',', '.'))
    if price >= WANTED_PRICE:
        diff = price - WANTED_PRICE
        print(f"It is still {diff} too expansive")
    else:
        print("Cheaper!!")
        send_mail()

def getPrice():
    page = requests.get(URL, headers=browser)
    soup=BeautifulSoup(page.content,"html.parser")
    title = soup.find("h1",{"class":"product-name"}).get_text().strip()
    price = soup.find("a", {"class": "price-label"}).get_text().strip()[1:8]

    print(title)
    print(price)
    return price

def send_mail():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("email", "password")

    subject = "Price fell down!"
    body = "https://www.buscape.com.br/fone-de-ouvido-e-headset/fone-de-ouvido-bluetooth-com-microfone-apple-airpods-2-estojo-sem-fio?_lc=88&q=airpods%20apple"

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        "email from xxxxxxx",
        "email to xxxxxxxx",
        msg
    )
    print(">>>>> HEY.. EMAIL HAS BEEN SENT!<<<<<<")

    server.quit()

if __name__=="__main__":
    while True:
        trackPrice()
        time.sleep(60)
