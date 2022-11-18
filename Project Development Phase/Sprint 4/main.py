from flask import Flask, render_template, request
from Model import ConnectDb, Account
import matplotlib.pyplot as plt
import numpy as np


app=Flask(__name__)
conn=ConnectDb.connect()
u_name = None

@app.route("/")
@app.route("/login",methods=['POST','GET'])
def login():
    if request.method=="POST" :
        creds = Account.login(conn,request)
        expenses  = Account.getExpenseData(conn,request)
        global u_name
        u_name = creds['USERNAME']
        print('loginpage',expenses)
        if(not creds):
            return "Invalid Email or password:("
        else:
            return render_template('home.html',email=creds['EMAIL'],expenses=expenses,name = u_name)
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
            return render_template('home.html',email=registered,expenses=expenses,name =u_name)
        else:
            return "Oops failed!!"
    return render_template('registerpage.html')


@app.route("/reteriveData",methods=['POST'])
def reteriveDetails():
    if request.method=="POST" :
        result = Account.reteriveDetails(conn, request)
        food=0
        enter=0
        shopping=0
        education=0
        others=0
        bill=0
        # print('Retrive Details:',result)
        for i in result:
            if i[0]== "food":
                food+=1
            elif i[0]=="Entertaiment":
                enter+=1
            elif i[0]=="Bills":
                bill+=1
            elif i[0]=="Others":
                others+=1
            elif i[0]=="Education":
                education+=1
            elif i[0]=="Groceries":
                shopping+=1
        print(food)    
        x=np.array([food,education,bill,shopping,enter,others])
        mylabel=["Food","Education","Bills","Groceries","Entertaiment","Others"]
        sep=[0.1,0.1,0.1,0.1,0.1,0.1]
        plt.pie(x,labels=mylabel,explode=sep)
        plt.legend()
        plt.show()
        if(result):
            return result
        else:
            return "Oops failed!!"
    return render_template('registerpage.html')


if __name__=="__main__":
    app.run(debug=True)
