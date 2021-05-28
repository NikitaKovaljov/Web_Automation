from flask import Flask
from flask_ngrok import run_with_ngrok
from twilio.rest import Client
import requests
import json
from bs4 import BeautifulSoup
import os
import time
import appscript

app = Flask(__name__)
appscript.app("Terminal").do_script("ngrok http 4000")

@app.route("/")
def hello():
    return "Server is running!"

if __name__ == '__main__':
    app.run(host = "localhost",port = 4000, debug = True)
