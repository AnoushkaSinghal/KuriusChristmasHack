from flask import Flask, request, jsonify, send_from_directory 

import os
import json
import time

from getDist import getDistanceFunction, DISTANCE_DRY_RESPONSE
from getBanks import getAvailableBanksFunction, GEOCODE_DRY_RESPONSE
from getQuestion import getQuestionFunction

###### End of imports #######

###### GLOBAL VARIABLES ######
DRY_RUN = True
app = Flask(__name__)
###### GLOBAL VARIABLES ######

###### Set up of API KEY ######
if not DRY_RUN:
	try:
		API_KEY = os.environ['GOOGLE_API_KEY']
	except:
		print('MISSING API KEY!')
		exit()
###### Set up of API KEY ######

@app.route('/getDistance', methods=['POST', 'GET'])
def getDistance():
	if DRY_RUN:
		return jsonify(DISTANCE_DRY_RESPONSE)
	else:
		addr1 = request.args['address1']
		addr2 = request.args['address2']
		return jsonify(getDistanceFunction(addr1, addr2, API_KEY))

@app.route('/getAvailableBanks', methods=['POST', 'GET'])
def getAvailableBanks():
	if DRY_RUN:
		return jsonify(GEOCODE_DRY_RESPONSE)
	else:
		addr = request.args['address']
		radius = int(request.args['radius'])
		return jsonify(getAvailableBanksFunction(addr, radius, API_KEY))

@app.route('/getQuestion', methods=['POST', 'GET'])
def getQuestion():
	number = int(request.args['number'])
	return jsonify(getQuestionFunction(number))

@app.route('/<path:path>') # For more security, add every path in a function
def send(path):
	return send_from_directory('..', path)

if __name__ == '__main__':
	app.run(host='localhost', port=8000, debug=True)

