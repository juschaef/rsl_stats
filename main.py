from flask import Flask 
from flask import render_template
from flask import request
from flask import redirect
import cv2
import pytesseract
import numpy
import re
import sqlite3
import os
from pprint import pprint

app = Flask(__name__, static_folder='static')

def match_stat(line):
	m = re.match(r"(.*) (.*)$", line)
	return (m.group(1), m.group(2))

def parse_stuff(stuff):
	stuff_dict = {}
	lines = stuff.splitlines()
	print(lines)
	set_match = re.match(r"SET: (.*)$", lines[0])
	main_match = re.match(r"(.*) (.*)$", lines[3])
	stuff_dict['set'] = set_match.group(1)
	stuff_dict['piece'] = lines[2]
	stuff_dict['main'] = match_stat(lines[3])
	stuff_dict['sub1'] = match_stat(lines[4])if len(lines) > 4 else None
	stuff_dict['sub2'] = match_stat(lines[5])if len(lines) > 5 else None
	stuff_dict['sub3'] = match_stat(lines[6])if len(lines) > 6 else None
	stuff_dict['sub4'] = match_stat(lines[7])if len(lines) > 7 else None
	return stuff_dict

@app.route("/",  methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		file = request.files['file']
		img = numpy.fromfile(request.files['file'], numpy.uint8)
		new_image = cv2.imdecode(img, cv2.IMREAD_UNCHANGED)
		new_image = cv2.cvtColor(new_image, cv2.COLOR_BGR2GRAY)
		new_image = cv2.convertScaleAbs(new_image, alpha=3.0, beta=0)
		text = pytesseract.image_to_string(1- new_image)
		print(text)
		print(80 * '=')
		stuff_dict = parse_stuff(os.linesep.join([s for s in text.splitlines() if s]))
		pprint(stuff_dict)
	return render_template('index.html')

if __name__ == "__main__":
    app.run()