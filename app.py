from flask import Flask,render_template
import numpy as np
import pandas as pd
import openpyxl

app = Flask(__name__)

data = pd.read_excel("2020-12-02.xlsx",engine='openpyxl')
mylist = tuple(map(tuple, data.to_numpy()))
heading = ("S.no","instrument_token","exchange_token","tradingsymbol","name","last_price","expiry","strike","tick_size","lot_size","instrument_type","segment","exchange")

@app.route('/')
def index():
    return render_template("index.html",heading = heading ,mylist = mylist)
