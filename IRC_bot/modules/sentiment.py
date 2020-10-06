import requests
import json

def get_sentiment(sentence):

    # Base URL for the sentiment analysis API
    url = 'https://sentim-api.herokuapp.com/api/v1/'
    
    # Setting headers and body as specified by the API docs
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    body = {'text': sentence}

    # Send the request and load the response into a dictionary
    response = requests.post(url, data=json.dumps(body), headers=headers)
    response_json = json.loads(response.text)

    # Get the sentence type (positive / negative) and the polarity
    sentence_type = response_json['result']['type']
    sentence_polarity = response_json['result']['polarity']

    return f'The sentence is {sentence_type} and its polarity is {sentence_polarity}'
