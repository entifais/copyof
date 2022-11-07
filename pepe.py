#!/usr/bin/env python
# -*- coding: utf-8 -*-"
#commap - by jero98772
from flask import Flask, render_template, request, flash, redirect ,session
import os
from tools.tools import *
app = Flask(__name__)

class webpage():
  @app.route("/cod1.html")
  def cod1():#Cels10428
    return render_template("cod1.html")
  @app.route("/cod2.html")
  def cod2():#Au10428
    return render_template("cod2.html")
  @app.route("/cod3.html")
  def cod3():#Eaf10428
    return render_template("cod3.html")
  @app.route("/null.html")
  def no():#Eaf10428
    return render_template("no.html")
  @app.route("/",methods=["GET","POST"])
  def index():
    if request.method=="POST":
     code=request.form["code"]
     code=code.title()
     if "Cels10428"==code:
      return redirect("cod1.html") 
     if "Arg10428"==code:
      return redirect("cod2.html")
     if "Eaf10428"==code:
      return redirect("cod3.html")
     else:
      return redirect("null.html")
    return render_template("index.html")
      
if __name__ == "__main__":
  app.run(debug=True,host="0.0.0.0",port=5000)
