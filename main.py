import requests
from bs4 import BeautifulSoup

hisse_url = "https://finance.yahoo.com/quote/NFLX?p=NFLX&.tsrc=fin-srch"

html_kod = requests.get(hisse_url)

#print(html_kod)
#print(html_kod.content)

# lxml kullanmak için pip install lxml çalıştırın
soup = BeautifulSoup(html_kod.content, 'lxml')

#print(soup.title.text)

sayfa_title = soup.find("title").get_text()

#print(sayfa_title)

header = soup.find_all('div', id='quote-header-info')[0]

hisse_title = header.find('h1').get_text()

#print(hisse_title)

hisse_fiyat = header.find('div', class_='My(6px) Pos(r) smartphone_Mt(6px)').find('span').get_text()

print(hisse_title + " - " + hisse_fiyat)
print('-------------------------')

table_info = soup.find('div', class_="D(ib) W(1/2) Bxz(bb) Pend(12px) Va(t) ie-7_D(i) smartphone_D(b) "
                                     "smartphone_W(100%) smartphone_Pend(0px) smartphone_BdY "
                                     "smartphone_Bdc($seperatorColor)")

for i in range(0,8):

    satirlar = table_info.find_all("tr")[i].find_all("td")

    #print(table_info)

    satir_baslik = satirlar[0].get_text()
    satir_deger = satirlar[1].get_text()

    print(satir_baslik + ": " + satir_deger)
