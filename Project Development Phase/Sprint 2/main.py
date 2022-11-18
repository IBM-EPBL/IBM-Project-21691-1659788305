from flask import Flask, render_template, request
from Model import ConnectDb, Account
import ibm_db
import json

app=Flask(__name__)
conn=ConnectDb.connect()

@app.route("/")
@app.route("/login",methods=['POST','GET'])
def login():
    if request.method=="POST" :
        creds = Account.login(conn,request)
        expenses  = Account.getExpenseData(conn,request)
        print('loginpage',expenses)
        if(not creds):
            return "Invalid Email or password:("
        else:
            return render_template('home.html',email=creds['EMAIL'],expenses=expenses)
    return render_template('loginpage.html')


@app.route("/register",methods=['POST','GET'])
def register():
    if request.method=="POST" :
        registered = Account.register(conn, request)
        if(registered):
            return render_template('loginpage.html', process="Registration Successful!")
        else:
            return render_template('registerpage.html',process="Email already exist!")
    return render_template('registerpage.html')


@app.route("/addExpense",methods=['POST'])
def addExpense():
    if request.method=="POST" :
        registered = Account.addExpense(conn, request)
        expenses  = Account.getExpenseData(conn,request)

        if(registered):
            return render_template('home.html',email=registered,expenses=expenses)
        else:
            return "Oops failed!!"
    return render_template('registerpage.html')


@app.route("/reteriveData",methods=['POST'])
def reteriveDetails():
    if request.method=="POST" :
        result = Account.reteriveDetails(conn, request)
        print('Retrive Details:',result)
        
        
        if(result):
            return result
        else:
            return "Oops failed!!"
    return render_template('registerpage.html')


if __name__=="__main__":
    app.run(debug=True)
