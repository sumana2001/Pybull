import urllib
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from urllib.error import HTTPError


def scrape(topic):
    wiki_query = str(topic)
    wiki_query = wiki_query.strip()

    # format query for GET request to Wikipedia
    wiki_query = wiki_query.replace(" ", "_")
    wiki_URL = 'https://en.wikipedia.org/wiki/' + wiki_query

    try:
        uClient = uReq(wiki_URL)
    except:
        raw_paragraph = " "
        return raw_paragraph, wiki_URL

    page_soup = soup(uClient.read(), "html.parser")
    uClient.close()

    for p in page_soup.find_all("p", {'class': 'mw-empty-elt'}):
        p.decompose()

    raw_paragraph = page_soup.find("div", {"class": "mw-parser-output"})
    raw_paragraph = raw_paragraph.p
    raw_paragraph = raw_paragraph.get_text()

    if raw_paragraph[-25:-1] == 'most commonly refers to:':
        options = page_soup.find_all("ul")[0]
        options = options.find_all('li')

        for i in range(len(options)):
            options[i] = options[i].get_text()
            options[i] = '\n- ' + options[i]
            raw_paragraph += options[i]

    elif raw_paragraph[-17:-1] == 'often refers to:':
        options = page_soup.find_all("ul")[0]
        options = options.find_all('li')

        for i in range(len(options)):
            options[i] = options[i].get_text()
            options[i] = '\n- ' + options[i]
            raw_paragraph += options[i]

    elif raw_paragraph[-14:-1] == 'may refer to:':
        options = page_soup.find_all("h2", {'class': ''})
        options = options[1:-2]

        for i in range(len(options)):
            options[i] = options[i].get_text()
            options[i] = '\n- ' + options[i][:-6]
            raw_paragraph += options[i]

    return raw_paragraph
