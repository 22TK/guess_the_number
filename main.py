from flask import Flask, render_template, request
from random import choice
from replit import db

app = Flask(__name__)

if 'guesses' not in db:
	db['guesses'] = []

if 'answer' not in db:
	db['answer'] = choice(list(range(1, 101)))

def checkNum(guess, answer):
	if guess > db['answer']: 
		return f'{guess} is too high' 
	elif guess < db['answer']:
		return f'{guess} is too low'
	else:
		return f'{guess} is correct' 
  

@app.route('/', methods=['GET', 'POST'])
def index():

	message = ''
	if request.method == 'POST':	
		guess = int(request.form['number_guess'])
		message = checkNum(guess, db['answer'])
		
	print(message)
	db['guesses'].append(message)
	return render_template('index.html', guesses=reversed(db['guesses']))
	


@app.route('/reset')
def reset():
	db['answer'] = choice(list(range(1, 101)))
	db['guesses'] = []
	return render_template('index.html', guesses=reversed(db['guesses']))


app.run(host='0.0.0.0', port=81)
