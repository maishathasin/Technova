# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from flask import Flask, escape, request
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from typing import Union
from model_API.model import model

app = Flask(__name__)
load_dotenv()

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)


@app.get("/model",methods=['GET'])
def read_stock(q: Union[str, None] = None): #optional parameter for now
    return model('pictures/banana and apple2.jpeg')

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    body = request.values.get('Body', None)
    resp = MessagingResponse()
    output = model('pictures/banana and apple2.jpeg')
    # Add a message
    if body == 'hi':
        resp.message('Hi welcome to Shelter X. Reply with "list" to see what we have in stock!')
    elif body == 'list':
        respond = ''
        for i in output:
            respond = respond + i + ':' + output[i] + '\n' 
            
        resp.message(respond)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)