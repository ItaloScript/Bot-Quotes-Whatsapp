from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse
from requests import get
from os import system
from bs4 import BeautifulSoup
from random import randint
import os,sys,time



def frase_gerador():
    count = randint(1,9656)
    count_id = randint(0,19)
    request = get(f"https://www.pensador.com/frases/{count}/")
    quotes_all = BeautifulSoup(request.text,"html.parser")
    quotes_fr = quotes_all.find_all(class_="frase")[count_id].get_text()
    quotes_author = quotes_all.find_all(class_="frase")[count_id].find_next_sibling().get_text()
    return(f"{quotes_fr} - {quotes_author}") 


# The session object makes use of a secret key.
SECRET_KEY = 'MY SECRET KEY'
app = Flask(__name__)
app.config.from_object(__name__)

# Try adding your own number to this list!


@app.route("/", methods=['GET', 'POST'])
def hello():
    global stage

    
    message_command = request.values.get('Body')
    print(message_command)
    system("pause")
    if "bot frase" in message_command.lower():
            message = frase_gerador()

        
    resp = MessagingResponse()
    resp.message(message)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)