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

class ActionPizzaCost(Action):

	def name(self) -> Text:
		return "action_pizza_cost"

	def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict]:
		pizza_data = {'small':50,'medium':100,'large':150}
		topping_data = {'tomato':50,'paneer':50,'onions':50,'Perreroni':50,'olives':50,'cheeze':50,'Corn':50}
		size,topping = '',''
		entities = tracker.latest_message['entities']
		for en in entities:
			if en['entity'] == 'size':
				size = en['value']
			if en['entity'] == 'topping':
				topping = en['value']
		print(entities)
		pizza_cost = pizza_data.get(size,0)
		topping_cost = topping_data.get(topping,0)
		total_cost=pizza_cost+topping_cost
		dispatcher.utter_message(text='Okay. Your order cost is {}'.format(total_cost))
		return []

