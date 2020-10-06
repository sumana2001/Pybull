import requests
import json

def random_cat_facts():
    try:
        url = 'https://cat-fact.herokuapp.com/facts/random'
        response = requests.get(url)
        response_json = json.loads(response.text)
        return "Cat Fact: " + response_json.get('text')
    except:
        return "Error No Cat Facts"
