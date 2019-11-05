'''
Created on 1 nov. 2019

@author: antonny
'''
import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="MercadoLibre"
)

