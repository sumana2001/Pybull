import requests
import json

def random_cat_pic():
    try:
        url = 'http://aws.random.cat/meow'
        response = requests.get(url)
        response_json = json.loads(response.text) 
        return "Here's a super cute cat pic: " + response_json.get('file')
    except:
        return "Error meow"
     