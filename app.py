import os
import sys
import time
import json
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

with app.app_context():
	print('blah')

@app.route('/')
def home(message=''):
	return(render_template('index.html', message=message))

@app.route('/parsejson', methods=['POST'])
def parse_json(message=None):
	try:
		data = json.loads(request.form['inputdata'])
		return(json.dumps(data, indent=4))
	except Exception as e:
		print(e, file=sys.stderr)
		return('Error: {0}'.format(e))
		

if __name__ == "__main__":
    app.run(host="0.0.0.0")
