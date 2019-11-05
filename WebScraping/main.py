'''
Created on 1 nov. 2019

@author: antonny
'''
from flask import Flask, render_template
from conexion import mydb
from Scraping import result, consultar

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

def scrap():
    return result

def consulta(self):      
    return consultar

if __name__ == '__main__':
    app.run()
    