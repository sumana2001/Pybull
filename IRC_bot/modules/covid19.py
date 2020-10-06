import requests
import json
import re

API_URL = 'https://api.covid19api.com/summary'

def get_covid_cases_by_country(country):
    """Gets the COVID-19 cases by the input country."""
    try:
        response = requests.get(API_URL)
        response_json = json.loads(response.text)

        # The API undergoes caching periodically,
        # during which it is unavailable.
        if response_json['Message'] == 'Caching in progress':
            return 'API Caching in progress, please try again later.'

        # Search for the country in the summary response
        country_data = next((data for data in response_json['Countries'] if data['Country'].lower() == country.lower()), {})

        if country_data:
            # Return the stats if the country is found
            covid_info = '\
                COVID-19 Cases for {Country} ({CountryCode}) - New Confirmed Cases: {NewConfirmed}, \
                    Total Confirmed Cases: {TotalConfirmed}, \
                        New Deaths: {NewDeaths}, \
                            Total Deaths: {TotalDeaths}, \
                                New Recovered Cases: {NewRecovered}, \
                                    Total Recovered Cases: {TotalRecovered}'
                
            # Remove any extra whitespace and fill the string
            # with keys from the data dictionary
            return re.sub(r"\s\s+" , " ", covid_info.format(**country_data))

        else:
            return 'Invalid Country Name'

    except Exception as e:
        print(e)
        return 'Error Fetching COVID-19 Data'


def get_global_covid_cases():
    """Gets the global COVID-19 Cases."""
    try:
        response = requests.get(API_URL)
        response_json = json.loads(response.text)

        # The API undergoes caching periodically,
        # during which it is unavailable.
        if response_json['Message'] == 'Caching in progress':
            return 'API Caching in progress, please try again later.'

        # Retrieve and return the global COVID-19 cases
        global_data = response_json['Global']

        global_covid_info = '\
            Global COVID-19 Cases - New Confirmed Cases: {NewConfirmed}, \
                Total Confirmed Cases: {TotalConfirmed}, \
                    New Deaths: {NewDeaths}, \
                        Total Deaths: {TotalDeaths}, \
                            New Recovered Cases: {NewRecovered}, \
                                Total Recovered Cases: {TotalRecovered}'

        # Remove any extra whitespace and fill the string
        # with keys from the data dictionary
        return re.sub(r"\s\s+" , " ", global_covid_info.format(**global_data))

    except Exception as e:
        print(e)
        return 'Error Fetching COVID-19 Data'