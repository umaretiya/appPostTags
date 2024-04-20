from app import app

from flask import render_template
from SmartApi import SmartConnect
import pyotp

file    = open("secret.txt").read().split()
api_key = file[0]
secret_key = file[1]
client_code = file[2]
secret_token = file[3]
password = file[4]

obj=SmartConnect(api_key=api_key)
data = obj.generateSession(client_code,password,pyotp.TOTP(file[3]).now())
feed_token = obj.getfeedToken()

@app.route('/')
def home():
    positions = obj.position()['data']
    return render_template('positions.html',context=positions)

@app.route('/login')
def login():
    return render_template('loginPopup.html')