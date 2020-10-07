import requests
import json

def random_joke():
    try:
        url = 'https://official-joke-api.appspot.com/random_joke'
        response = requests.get(url)
        response_json = json.loads(response.text)
        joke_setup = response_json.get('setup')
        joke_punchline = response_json.get('punchline')

        final_joke = joke_setup + ' ' + joke_punchline

        return final_joke

    except Exception as e:
        # TODO: Handle correct exceptions properly
        print(e)
        return "Error Beep Boop"

def random_chuck_joke():
    url = 'https://api.chucknorris.io/jokes/random'
    try:
        response = requests.get(url)
        response_json = json.loads(response.text) 
        return response_json.get('value')
    except:
        return 'Chuck went on vacation...'
     