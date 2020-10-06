from bs4 import BeautifulSoup
import lxml.html
import requests

def urban_term(term):
    try:
        url = "http://urbandictionary.com/define.php?term={0}".format(term)
        resource = BeautifulSoup(requests.get(url).content, "lxml")
        content = resource.find('div', {"class":"meaning"})
        if content is None:
            content = "¯\\_(ツ)_/¯"
        else:
            content = resource.find('div', {"class":"meaning"}).text.strip()
        return content

    except Exception as e:
        # TODO: Handle correct exceptions properly
        print(e)
        return "Error Beep Boop"
