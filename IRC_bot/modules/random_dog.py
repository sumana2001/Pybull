import requests
import json

def random_dog_pic():
    try:
        url = 'https://dog.ceo/api/breeds/image/random'
        response = requests.get(url)
        response_json = json.loads(response.text) 
        return "Here's a super cute doc pic: " + response_json.get('message')
    except:
        return "No dogs available today :/"
     
