from urllib.parse import urlencode
from geopy.distance import distance

import pickle
import requests
import pandas as pd

###### GLOBAL VARIABLES ######
GEOCODE_URL = 'https://maps.googleapis.com/maps/api/geocode/json?'

GEOCODE_DRY_RESPONSE = [
	{
		'name': 'Food Bank 1',
		'address': 'Address 1',
		'phone': 'Phone Number 1'
	},
	{
		'name': 'Food Bank 2',
		'address': 'Address 2',
		'phone': 'Phone Number 2'
	},
	{
		'name': 'Food Bank 3',
		'address': 'Address 3',
		'phone': 'Phone Number 3'
	}
]

with open('FoodBanks.pickle', 'rb') as f:
	ALL_FOOD_BANKS = pickle.load(f)
###### GLOBAL VARIABLES ######

def _distance(point1, point2):
	return distance(point1, point2).km

def _getLatLong(address, API_KEY):
	data = {
		'address': address,
		'key': API_KEY
	}

	response = requests.get(GEOCODE_URL + urlencode(data))
	info = response.json()['results'][0]['geometry']['location']

	return info['lat'], info['lng']

def _available(point1, df, radius):
	return df[df.apply(lambda x: _distance(point1, (x['latitude'], x['longitude'])), axis=1) < radius]

def getAvailableBanksFunction(address, radius, API_KEY):
	point1 = _getLatLong(address, API_KEY)

	# Filtering by radius
	availableBanks = _available(point1, ALL_FOOD_BANKS, radius)

	return_statement = availableBanks.drop(['latitude', 'longitude'], axis=1)
	return return_statement.to_json(orient="records")