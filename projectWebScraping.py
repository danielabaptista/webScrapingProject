#libraries needed
from bs4 import BeautifulSoup
import requests
import smtplib
import time
import datetime 

#connect to the website
#URL = 'https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_3?dchild=1&keywords=data%2Banalyst%2Btshirt&qid=1626655184&sr=8-3&customId=B0752XJYNL&th=1'
URL = 'https://www.amazon.com/Outerspace-Science-Teacher-Astronaut-Novelty/dp/B01MEH0Q5M/ref=sr_1_20_sspa?crid=3CODESS0CYFLG&dib=eyJ2IjoiMSJ9.aDwY2PLjyErgLtBfmv7z1jTULBgiF3sK-0SPbmq5EtXyafnb6lFXV83lcmhE1285iapS1xj8g7ZMysY6XyCJBj-E0tTg_2NdJlSayMcvIKxRg3DnyjvZZrWflWq8vft5rjN6SSySTivG-hv-4-ndyHMoMq1C3enZoVIhUX4shJ5nZvxZDPGHd5HNP0AqKFmly-vta7Cp7MyJD5T33rHu4xGy1C0Up9PG3jlR-BWlUoNbfkYqtMAXvsYsUa8Co8pUzbyNuw7P7gceXuabcn38MGmwQUoaSumkKeuR9zI2ORg.aIj3KLZN7FHoYNuigdPQJK1oupy-g9JsLqkCOkEdvDE&dib_tag=se&keywords=coding+tshirt&qid=1711034190&sprefix=coding+tshirt%2Caps%2C338&sr=8-20-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9tdGY&psc=1'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'DNT': '1',
    'Connection': 'close',
    'Upgrade-Insecure-Requests': '1'
}

page = requests.get(URL, headers = headers)

soup1 = BeautifulSoup(page.content, "html.parser")
soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find(id='productTitle').get_text()

price = soup2.find('span', class_='aok-offscreen').get_text()

print(title)
print(price)


