# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 11:00:14 2021

@author: darshanRaghunath
"""
#import the modules

from flask import Flask,redirect, url_for, request
from flask_cors import CORS, cross_origin
from mysql.connector import Error
import mysql.connector
import json

#Details to connect to database

host_name="sql6.freesqldatabase.com"
user_name="sql6447546"
user_password="mTZ37tUA1E"
db_name="sql6447546"
Port=3306

# function to create a connection 


def create_db_connection(host_name, user_name, user_password, db_name,Port):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name,
            port=Port
        )
        print("MySQL Database successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


# function to write in to the database


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")



# function to read from the database

def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")

#The basics of flask

connection = create_db_connection(host_name, user_name, user_password, db_name,Port)
app = Flask(__name__)
CORS(app ,resources={r"/api/*":{"origins":"*"}})
app.config['CORS_HEADERS'] = 'Content-Type'
@app.route('/')
@cross_origin()
def hello_world():
    return 'hello world'


@app.route('/success/<name>')
@cross_origin()
def hello_name(name):
   return 'Hello %s!' % name

#both post aswell as get  


@app.route('/opinion',methods = ['POST', 'GET'])
@cross_origin()
def login():  
   if request.method == 'POST':
       print("Hello")
       connection = create_db_connection(host_name, user_name, user_password, db_name,Port)
       user = request.json["Name"]
       url3 = request.json["url"]
       print(user)
       print(type(user))
       query = "INSERT INTO pvptable (Personid , Name, url) VALUES" + "(Null ,'" +user + "','"+ url3+"')"

       execute_query(connection, query)
       query2 = "SELECT * FROM pvptable ORDER BY Personid DESC"
       result=read_query(connection,query2)
       jsonObj = json.dumps(result)
       return jsonObj
        

   else:
      connection = create_db_connection(host_name, user_name, user_password, db_name,Port)
      query2 = "SELECT * FROM pvptable ORDER BY Personid DESC"
      result=read_query(connection,query2)
      print("list")
      jsonObj = json.dumps(result)
      print(jsonObj)
      print(type(jsonObj))
      return jsonObj


if __name__ == '__main__':
 
    app.run(debug=True)
