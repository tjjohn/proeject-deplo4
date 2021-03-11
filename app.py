# -*- coding: utf-8 -*-
"""
Created on Tue Mar  11 11:41:04 2021

@author: tj john
"""
from flask import Flask, request,render_template
import numpy as np
import pickle
import pandas as pd

app=Flask(__name__)

#pickle_in = open("lr.pkl","rb")
#predict_Rem_Ind=pickle.load(pickle_in)


@app.route('/')                        # fn for homepage
def welcome():
    return render_template("index.html")

@app.route('/basepredict', methods =["GET", "POST"]) 
def predict(): 
    if request.method == "POST":  
       Department_Name = request.form.get("Department_Name") 
       Class_Name = request.form.get("Class_Name") 
       Division_Name = request.form.get("Division_Name") 
       Age= request.form.get("Age") 
       Review = request.form.get("Review") 
       return "Entereed details "+ Department_Name + Class_Name + Division_Name+ Age +   Review 
   
    if request.method == "POST1": 
       Department_Name = request.form.get("Department_Name") 
       Class_Name = request.form.get("Class_Name") 
       Division_Name = request.form.get("Division_Name") 
       Age= request.form.get("Age") 
       Review = request.form.get("Review") 
       return "Entereed details "+ Department_Name + Class_Name + Division_Name
    
    return render_template("index.html") 

if __name__=='__main__':
    app.run()
    