from urllib.parse import urlencode
import requests

DISTANCE_MATRIX_URL = 'https://maps.googleapis.com/maps/api/distancematrix/json?'

DISTANCE_DRY_RESPONSE = {
		'driving': {
			'distance': '10km',
			'time': '35 mins'
		},
		'walking': {
			'distance': '11km',
			'time': '2 hours 5 mins'
		}
	}

def getDistanceFunction(address1, address2, API_KEY):
	data = {
		'origins': address1,
		'destinations': address2,
		'units': 'metric',
		'mode': 'driving',
		'key': API_KEY
	}

	# Getting driving time and distance
	drivingResponse = requests.get(DISTANCE_MATRIX_URL + urlencode(data))
	drivingInfo = drivingResponse.json()['rows'][0]['elements'][0]

	# Getting walking time and distance
	data['mode'] = 'walking'
	walkingResponse = requests.get(DISTANCE_MATRIX_URL + urlencode(data))
	walkingInfo = walkingResponse.json()['rows'][0]['elements'][0]

	allInfo = {
		'driving': {
			'distance': drivingInfo['distance']['text'],
			'time': drivingInfo['duration']['text']
		},
		'walking': {
			'distance': walkingInfo['distance']['text'],
			'time': walkingInfo['duration']['text']
		}
	}

	return allInfo