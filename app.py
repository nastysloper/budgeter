from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/test')
def running():
	return "running!"

@app.route('/')
def main():
	return render_template('index.html')