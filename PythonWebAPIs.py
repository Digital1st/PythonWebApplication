from flask import Flask , render_template, request ,jsonify
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
      
    
        
        return render_template('1.html')

    else:
        return "error no it field provided"

if __name__=="__main__":
    app.run()
    