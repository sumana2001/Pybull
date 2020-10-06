import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

def get_zodiac_number(sign):
    sign = sign.lower()
    sign_dict = {'aries':1, 'taurus':2, 'gemini':3, 'cancer':4, 'leo':5, 'virgo':6,
    'libra':7, 'scorpio':8, 'sagittarius':9, 'capricorn':10, 'aquarius':11, 'pisces':12}
    if sign in sign_dict:
        return sign_dict[sign]
    else:
        return -1

def get_horoscope(sign):
    zodiac_num = get_zodiac_number(sign)
    if zodiac_num < 0:
        return "I don't know this sign"
        
    horo_link = 'https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign={}'.format(zodiac_num)

    try:
        htmlhub = urlopen(horo_link)
    except:
        return 'No horoscope for you today'

    page = soup(htmlhub.read(), "html.parser")
    htmlhub.close()

    horo_first = page.find("div", {'class': 'main-horoscope'})
    horo_par = horo_first.find("p", {'class': ''})
    horo_text = horo_par.get_text()
    return horo_text