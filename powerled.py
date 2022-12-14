#!/usr/bin/env python
from flask import Flask, render_template
from termcolor import colored
import os
import requests
app = Flask.Flask(__name__)
app.config["DEBUG"] = True
def ledOn():
   os.system("echo 1 | sudo tee /sys/class/leds/led[0]/brightness")
   os.system("echo 0 | sudo tee /sys/class/leds/led[1]/brightness")
   requests.get("192.168.0.122:8080/on")
   requests.get("192.168.0.123:8080/on")
   print (colored("On", "green"))
def ledOff():
   os.system("echo 0 | sudo tee /sys/class/leds/led[0]/brightness")
   os.system("echo 0 | sudo tee /sys/class/leds/led[1]/brightness")
   requests.get("192.168.0.122:8080/off")
   requests.get("192.168.0.123:8080/off")
   print (colored("Off", "red"))

@app.route('/gui')
def home():
    return render_template("index.html")
@app.route('/on')
def on():
    ledOn()
    return 'Led is on'

@app.route('/off')
def off():
    ledOff()
    return 'Led is off'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
