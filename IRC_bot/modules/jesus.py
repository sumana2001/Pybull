import requests as rq
import json

#rq = rq.get("https://jesusapi.000webhostapp.com/api")
#rq.text

#print(rq.text)

def jesus():
    try:
        url = 'https://tronalddump.io/random/quote'
        response = rq.get(url)
        response_json = json.loads(response.content)
        return "Have a blessed day: " + response_json.get('value')
    except:
        return "Jesus says Good day!"


