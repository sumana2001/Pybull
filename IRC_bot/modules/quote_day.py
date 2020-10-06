import requests
import json

def quote_of_the_day():
    try:
        url = 'https://quotes.rest/qod/'
        response = requests.get(url)
        response_json = json.loads(response.text)
        try:  # Only 10 requests allowed per hour
            quote = response_json[u'contents'][u'quotes'][0][u'quote']
            quote_author = response_json[u'contents'][u'quotes'][0][u'author']
        except KeyError:
            quote = response_json[u'error'][u'code']
            quote_author = response_json[u'error'][u'message']
        
        quote_of_day = str(quote) + ' - ' + str(quote_author)
        return quote_of_day

    except Exception as e:
        # TODO: Handle correct exceptions properly
        print(e)
        return "Error Beep Boop"