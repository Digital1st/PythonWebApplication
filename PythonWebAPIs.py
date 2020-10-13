from flask import Flask , render_template, request ,jsonify
import sqlite3
import mysql.connector


app=Flask(__name__)
@app.route("/registration/",methods=['GET'])


def registration():
    if 'pass' in request.args:
        pass_=str(request.args['pass'])
        usern=str(request.args['uname'])
        return "pass="+str(pass_)+ " user="+usern+ "Success"
    else:
        return "error no it field provided"
    return render_template('1.html')


@app.route("/login/",methods=['POST'])
def login():
    if 'pass' in request.args:
        pass_=str(request.args['pass'])
        usern=str(request.args['uname'])
    
        print( "pass="+str(pass_)+ " user="+usern+ "Success")
    
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

       
       # conn.row_factory = dict_factory
        
       
    

        all_Objects = cur.execute('SELECT * FROM Objects;').fetchall()

    return jsonify(all_Objects)        
        
    


@app.route("/create/",methods=['GET'])

def createall():
    if 'token' in request.args:
        token=str(request.args['token'])

        conn = sqlite3.connect('database.db')
       # conn.row_factory = dict_factory
        
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS Users (id integer PRIMARY KEY,name text NOT NULL,pass text,end_date text)")
        cur.execute("CREATE TABLE IF NOT EXISTS Tokens (id integer PRIMARY KEY,name text NOT NULL,begin_date text,end_date text)")
        cur.execute("CREATE TABLE IF NOT EXISTS Objects (id integer PRIMARY KEY,name text NOT NULL,begin_date text,end_date text)")

        cur.execute("insert into Objects values ('1','TestUserName','PWD','01.01.9999')")


        all_Objects = cur.execute('SELECT * FROM Objects;').fetchall()

    return jsonify(all_Objects)        
    #else:
     #   return render_template('1.html')        

if __name__=="__main__":
    app.run()
    