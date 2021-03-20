import requests
from bs4 import BeautifulSoup

hisse_url = "https://www.vestel.com.tr/vestel-kmi-9701-g-kurutma-makinesi"

html_kod = requests.get(hisse_url)

soup = BeautifulSoup(html_kod.content, 'lxml')

bilgi_bar = soup.find('div', class_='price').find('span', class_="discounted")

print(bilgi_bar.get_text())