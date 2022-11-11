from flask import Flask, render_template, request
from Model import ConnectDb, Account

app=Flask(__name__)
conn=ConnectDb.connect()

@app.route("/")
@app.route("/login",methods=['POST','GET'])
def login():
    if request.method=="POST" :
        creds = Account.login(conn,request)
        #print("main", creds)       
        if(not creds):
            return "Invalid Email or password:("
        else:
            return "Logged in Successfully!"
    return render_template('loginpage.html')

@app.route("/register",methods=['POST','GET'])
def register():
    if request.method=="POST" :
        registered = Account.register(conn, request)
        if(registered):
            return render_template('loginpage.html')
        else:
            return "Email already Exist"
    return render_template('registerpage.html')


if __name__=="__main__":
    app.run(debug=True)
