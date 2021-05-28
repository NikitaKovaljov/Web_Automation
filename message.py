from flask import Flask, request, redirect
from flask_ngrok import run_with_ngrok
from twilio.rest import Client
from twilio.twiml.messaging_response import Message, MessagingResponse
import os
import time
import appscript
import socket
import sys



while True:

    time.sleep(30)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('localhost',4000))

    if result == 0:
        print("Server is up")
    else:
        account_sid = 'ACdebb7ce9eb55b027879a3b3fbacf2c52'
        auth_token = '64728e568e527d3ff5b5f511f9bc516e'
        client = Client(account_sid, auth_token)

        message = client.messages \
                        .create(
                            body="Server is down",
                            from_='+17372048573',
                            to='+37256966250'
                        )

        second = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        another = second.connect_ex(('localhost',5000))

        if another == 0:
            print("port already in use, and waiting for your response")
        else:
            app = Flask(__name__)
            run_with_ngrok(app)

            @app.route ("/message", methods = ['GET','POST'])

            def incoming_sms():
                body = request.values.get('Body',None)
                resp = MessagingResponse()

                if body == "Start":
                    appscript.app("Terminal").do_script("python3 /Users/nikitakovaljov/Desktop/Scripting\ Language/assignment6.py")
                elif body == "Down":
                    resp.message("Server will be down")
                return str(resp)

            if __name__ == "__main__":
                app.run() 
