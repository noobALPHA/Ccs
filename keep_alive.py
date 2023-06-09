from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Bot is online!"

def run():
  app.run(host='0.tcp.ap.ngrok.io',port=11906)

def live():  
    t = Thread(target=run)
    t.start()