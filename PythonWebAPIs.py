from flask import Flask , render_template, request ,jsonify
import sqlite3
from datetime import datetime,timedelta
from random import random,seed

app=Flask(__name__)
@app.route("/registration/",methods=['GET'])

#function for registration of the new users
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

#function for login on 
@app.route("/login/",methods=['GET'])
def login():
    if 'pass' in request.args:
        passs_=str(request.args['pass'])
        usern=str(request.args['uname'])
        conn = sqlite3.connect('database.db')
        
        cur = conn.cursor()
        

      
        all_Users = cur.execute('SELECT * FROM Users where name=? and pass=?;',(usern,passs_)).fetchall()
        if all_Users is not None:
            userid=all_Users[0][0]
            token=random()*10000
            now=datetime.now()
            #exp is expiration timedate for token , it is for 10 minutes 
            exp=datetime.now()+timedelta(minutes=10)
            #inserting temporary token into tokens table
            cur.execute("insert into Tokens values (?,?,?,?)",(token,userid,now,exp))

        conn.commit()
        conn.close()
        #returning token
        return jsonify(token)
    else:
        return "error no it field provided"
#function for creating new objects
@app.route("/items/new/",methods=['POST'])
def newitem():
    if 'token' in request.args:
        token=str(request.args['token'])
        objectparam=str(request.args['obparam'])
        conn = sqlite3.connect('database.db')
        #querying tokens table to get userid
        cur = conn.cursor()
        all_Tokens = cur.execute('SELECT * FROM Tokens where name=?;',token).fetchall()
        userid=all_Tokens[1][0]
        exptime=all_Tokens[3][0]
        #converting to datetime
        date_time_obj = datetime.datetime.strptime(exptime, '%Y-%m-%d %H:%M:%S.%f')
       
        if date_time_obj.time() > datetime.now().time():
            cur.execute("insert into Objects values ('149',objectparam['name'],userid,'01.01.9999')")

            conn.commit()

        print( "pass="+str(pass_)+ " user="+usern+ "Success")
    
    else:
        return "error no it field provided"

@app.route("/delete/",methods=['DELETE'])
def deleteitem():
    if 'token' in request.args:
        token=str(request.args['token'])
        conn = sqlite3.connect('database.db')
        #querying tokens table to get userid
        cur = conn.cursor()
        all_Tokens = cur.execute('SELECT * FROM Tokens where name=?;',token).fetchall()
        userid=all_Tokens[0][1]
        exptime=all_Tokens[0][3]
        #converting to datetime
        date_time_obj = datetime.datetime.strptime(exptime, '%Y-%m-%d %H:%M:%S.%f')
       
        if date_time_obj.time() > datetime.now().time():
       
    
            #deleting objects table for objects for only certain user
            all_Objects = cur.execute('DELETE * FROM Objects where userid=?;',userid).fetchall()

#function for querying items
@app.route("/items/",methods=['GET'])
def getitemslist():
    if 'token' in request.args:
        token=str(request.args['token'])
        conn = sqlite3.connect('database.db')
        #querying tokens table to get userid
        cur = conn.cursor()
        all_Tokens = cur.execute('SELECT * FROM Tokens where name=?;',token).fetchall()
        userid=all_Tokens[0][1]
        exptime=all_Tokens[0][3]
        #converting to datetime
        date_time_obj = datetime.datetime.strptime(exptime, '%Y-%m-%d %H:%M:%S.%f')
       
        if date_time_obj.time() > datetime.now().time():
       
    
            #querying objects table for objects for only certain user
            all_Objects = cur.execute('SELECT * FROM Objects where userid=?;',userid).fetchall()

    return jsonify(all_Objects)        
        
    


@app.route("/create/",methods=['GET'])
#creating all tables in the database
def createall():
    if 'token' in request.args:
        token=str(request.args['token'])

        conn = sqlite3.connect('database.db')
        
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS Users (id integer PRIMARY KEY,name text NOT NULL,pass text,end_date text)")
        cur.execute("DROP TABLE Tokens")
        cur.execute("CREATE TABLE Tokens (name text NOT NULL,userid integer,begin_date text,end_date text)")
        cur.execute("CREATE TABLE IF NOT EXISTS Objects (id integer PRIMARY KEY,name text NOT NULL,userid integer,end_date text)")

        cur.execute("insert into Objects values ('149','TestObjectName','01.01.2020','01.01.9999')")

        conn.commit()

        all_Objects = cur.execute('SELECT * FROM Users;').fetchall()
        conn.close()
    return jsonify(all_Objects)        
    #else:
     #   return render_template('1.html')        

if __name__=="__main__":
    app.run()
    