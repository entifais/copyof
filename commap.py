#!/usr/bin/env python
# -*- coding: utf-8 -*-"
#commap - by jero98772
from flask import Flask, render_template, request, flash, redirect ,session
import os
import pandas as pd
from tools.tools import *
app = Flask(__name__)
DATAPATH="static/data/data.csv"
MAPNAME="map.html"
if not os.path.isfile(DATAPATH):
  writetxt(DATAPATH,"name,contact,lat,lng")
class webpage():
  @app.route("/")
  def cod2():
    return render_template("cod2.html")
  @app.route("/")
  def cod1():#Cels10428
    return render_template("cod1.html")
  @app.route("/",methods=["GET","POST"])
  def index():
    if request.method=="POST":
     name=request.form["name"]
    return render_template("index.html")
      
if __name__ == "__main__":
  app.run(debug=True,host="127.0.0.1",port=5000)
