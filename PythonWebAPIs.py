from flask import Flask , render_template, request ,jsonify
import sqlite3
from datetime import datetime,timedelta
from random import random,seed

app=Flask(__name__)
@app.route("/registration/",methods=['GET'])


def registration():
    if 'pass' in request.args:
        passs_=str(request.args['pass'])
        usern=str(request.args['uname'])

        conn = sqlite3.connect('database.db')
        
        cur = conn.cursor()
        

        cur.execute("insert into Users values ('111',?,?,'01.01.9999')",(usern,passs_))

        conn.commit()
        conn.close()



        return "pass="+str(passs_)+ " user="+usern+ "Success"
    else:
        return "error no pass field provided"
    return render_template('1.html')


@app.route("/login/",methods=['GET'])
def login():
    if 'pass' in request.args:
        passs_=str(request.args['pass'])
        usern=str(request.args['uname'])
        conn = sqlite3.connect('database.db')
        
        cur = conn.cursor()
        

      
        all_Users = cur.execute('SELECT * FROM Users where name=? and pass=?;',(usern,passs_)).fetchall()
        token=random()*10000
        now=datetime.now()
        exp=datetime.now()+timedelta(minutes=10)
        cur.execute("insert into Tokens values (?,?,?,?)",(token,usern,now,exp))

        conn.commit()
        conn.close()

        return jsonify(token)
    else:
        return "error no it field provided"

@app.route("/items/new/",methods=['POST'])
def newitem():
    if 'token' in request.args:
        token=str(request.args['token'])
        objectparam=str(request.args['obparam'])
    
        print( "pass="+str(pass_)+ " user="+usern+ "Success")
    
    else:
        return "error no it field provided"

@app.route("/delete/",methods=['DELETE'])
def deleteitem():
    if 'token' in request.args:
        token=str(request.args['token'])
        id=str(request.args['id'])
    
        print( "pass="+str(pass_)+ " user="+usern+ "Success")
    
    else:
        return "error no it field provided"

@app.route("/items/",methods=['GET'])
def getitemslist():
    if 'token' in request.args:
        token=str(request.args['token'])
        conn = sqlite3.connect('database.db')
        
        cur = conn.cursor()
       

       
        
       
    

        all_Objects = cur.execute('SELECT * FROM Tokens;').fetchall()

    return jsonify(all_Objects)        
        
    


@app.route("/create/",methods=['GET'])

def createall():
    if 'token' in request.args:
        token=str(request.args['token'])

        conn = sqlite3.connect('database.db')
        
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS Users (id integer PRIMARY KEY,name text NOT NULL,pass text,end_date text)")
        cur.execute("DROP TABLE Tokens")
        cur.execute("CREATE TABLE Tokens (name text NOT NULL,user text,begin_date text,end_date text)")
        cur.execute("CREATE TABLE IF NOT EXISTS Objects (id integer PRIMARY KEY,name text NOT NULL,begin_date text,end_date text)")

        cur.execute("insert into Objects values ('119','TestObjectName','01.01.2020','01.01.9999')")

        conn.commit()

        all_Objects = cur.execute('SELECT * FROM Users;').fetchall()
        conn.close()
    return jsonify(all_Objects)        
    #else:
     #   return render_template('1.html')        

if __name__=="__main__":
    app.run()
    