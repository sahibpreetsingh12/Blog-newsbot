# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
import random

import urllib3


from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class ActionHelloUSA(Action):

    def name(self) -> Text:
        return "action_hello_usa"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        headers = {
            'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
        }

        url = ('https://newsapi.org/v2/top-headlines?'
               'country=us&'
               'apiKey=45a95279caaa429e8951aaab6a90086f')

        response = requests.get(url,headers=headers, verify=False)

        obj = json.loads(response.text)

        index = random.randint(0, obj['totalResults'])

        output = obj['articles'][index]['title'] + ' too read further ' + obj['articles'][index]['url']

        dispatcher.utter_message(text=output)

        return []


class ActionHelloGermany(Action):

    def name(self) -> Text:
        return "action_hello_germany"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        headers = {
            'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
        }

        url = ('https://newsapi.org/v2/top-headlines?'
               'country=de&'
               'apiKey=45a95279caaa429e8951aaab6a90086f')

        response = requests.get(url,headers=headers, verify=False)

        obj = json.loads(response.text)

        index = random.randint(0, obj['totalResults'])

        output = obj['articles'][index]['title'] + ' too read further ' + obj['articles'][index]['url']

        dispatcher.utter_message(text=output)

        return []


class CryptoSection(Action):

    def name(self) -> Text:
        return "action_crypto-section"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        headers = {
            'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
        }

        url = 'https://newsapi.org/v2/top-headlines?q=crypto&apiKey=45a95279caaa429e8951aaab6a90086f'

        response = requests.get(url, headers=headers, verify=False)
        # json_data = json.dumps(response.json())
        # obj = json.loads(json_data)
        obj = json.loads(response.text)

        index = random.randint(0, obj['totalResults'])

        output = obj['articles'][index]['title'] + ' too read further ' + obj['articles'][index]['url']
        dispatcher.utter_message(text=output)

        return []

