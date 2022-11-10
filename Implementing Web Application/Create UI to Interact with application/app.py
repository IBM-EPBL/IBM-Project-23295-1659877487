# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, url_for, session
import re

  
app = Flask(__name__)
  
app.secret_key = 'a'

@app.route('/')

def homer():
    return render_template('index.html')


@app.route('/login',methods =['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/register', methods =['GET', 'POST'])
def register():
    
    return render_template('register.html')




    
if __name__ == '__main__':
   app.run(host='0.0.0.0',port=8080)
