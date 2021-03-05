import json
import requests


class v2:
    api_key = None

    def __init__(self, api_key):
        self.api_key = api_key

    def holidays(self, parameters):
        url = 'https://calendarific.com/api/v2/holidays?'

        if 'api_key' not in parameters:
            parameters['api_key'] = self.api_key

        response = requests.get(url, params=parameters)
        data = json.loads(response.text)

        if response.status_code != 200:
            if 'error' not in data:
                data['error'] = 'Unknown error.'

        return data

    def countries(self, parameters):
        url = 'https://calendarific.com/api/v2/countries?'

        if 'api_key' not in parameters:
            parameters['api_key'] = self.api_key

        response = requests.get(url, params=parameters)
        data = json.loads(response.text)

        if response.status_code != 200:
            if 'error' not in data:
                data['error'] = 'Unknown error.'

        return data
