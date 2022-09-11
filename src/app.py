import os

import requests
from dotenv import load_dotenv
from flask import Flask, render_template

app = Flask(__name__)

load_dotenv()


@app.route('/')
def cat():
    resp = requests.get('https://api.thecatapi.com/v1/images/search')
    resp_json = resp.json()
    url = resp_json[0]['url']
    return render_template('index.html', title='Cat', image_url=url)


@app.route('/dog')
def dog():
    resp = requests.get('https://api.thedogapi.com/v1/images/search')
    resp_json = resp.json()
    url = resp_json[0]['url']
    return render_template('index.html', title='Dog', image_url=url)


if (__name__ == '__main__'):
    DEFAULT_PORT = 5000
    port = os.getenv('PORT') if os.getenv('PORT') is not None else DEFAULT_PORT

    app.run(port=port)
