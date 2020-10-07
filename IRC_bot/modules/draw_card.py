import requests
import json

def draw_card():
    try:
        url = 'https://deckofcardsapi.com/api/deck/new/draw/?count=1'
        response = requests.get(url)
        response_json = json.loads(response.text) 
        return "Here's your card: " + str(response_json['cards'][0]['value']).capitalize() + " of " + str(response_json['cards'][0]['suit']).capitalize() + ". " + response_json['cards'][0]['image']
    except:
        return "Oops, lost the card..."
     