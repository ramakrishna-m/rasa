# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class ActionPizzaOrder(Action):

	def name(self) -> Text:
		return "action_pizza_cost"

	def submit(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict]:
		data = {'small':50,'medium':100,'large':150}
		entities = tracker.latest_message['entities']
		for en in entities:
			if en['entity'] == 'size':
				size = en['value']
		cost = data.get(size,0)
		dispatcher.utter_message(text='Okay. Your order cost is {}'.format(cost))
		return []

