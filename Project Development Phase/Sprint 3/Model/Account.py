import ibm_db
from flask import Flask, render_template, request
from datetime import datetime
from calendar import month_name

def login(conn,request):
    email = request.form['email']
    password = request.form['password']
    sql =  f"select * from udetails where email='{email}' and password='{password}' "
    out = ibm_db.exec_immediate(conn,sql)
    return ibm_db.fetch_assoc(out)

   
def register(conn, request):
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']

    sql = f"select email from udetails;"
    out = ibm_db.exec_immediate(conn,sql)
    dictionary = ibm_db.fetch_both(out)

    while dictionary != False:
        
        if(dictionary['EMAIL']==email):
            print("Email already exist")
            return False
        dictionary = ibm_db.fetch_both(out)

    sql = f"insert into udetails (username, email, password) values ('{username}','{email}','{password}');"
    out = ibm_db.exec_immediate(conn,sql)

    return True


def addExpense(conn,request):
    expenseName = request.form['expensename']
    expenseValue = request.form['expensevalue']
    expenseCategory = request.form['expensecategory']
    expenseDate = request.form['expensedate']
    email = request.form['email']

    sql = f"insert into EXPENSE (EMAIL,EXPENSENAME,EXPENSE,CATEGORY,EXPENSEDATE) values ('{email}','{expenseName}','{expenseValue}','{expenseCategory}','{expenseDate}');"
    try:
        out = ibm_db.exec_immediate(conn,sql)
        return email
    except:
        return False

    
def getExpenseData(conn,request): # key year, value list of months
    email = request.form['email'];
    sql =  f"select * from expense where email='{email}'"
    out = ibm_db.exec_immediate(conn,sql)
    dictionary = ibm_db.fetch_both(out)
    monthYear = {}
    
    if(dictionary):
        monthYear = {dictionary['EXPENSEDATE'].strftime("%Y"):[dictionary['EXPENSEDATE'].strftime("%B"),]}
        while dictionary != False:
            print(dictionary['EXPENSEDATE'].strftime("%B"), dictionary['EXPENSEDATE'].strftime("%Y"))
            if(dictionary['EXPENSEDATE'].strftime("%Y") in monthYear):
                if(dictionary['EXPENSEDATE'].strftime("%B") not in monthYear[dictionary['EXPENSEDATE'].strftime("%Y")]):
                    monthYear[dictionary['EXPENSEDATE'].strftime("%Y")].append(dictionary['EXPENSEDATE'].strftime("%B"))
            else:
                monthYear[dictionary['EXPENSEDATE'].strftime("%Y")] = []
                monthYear[dictionary['EXPENSEDATE'].strftime("%Y")].append(dictionary['EXPENSEDATE'].strftime("%B"))
            dictionary = ibm_db.fetch_both(out) 

        #months sorting
        month_lookup = list(month_name)
        for i in monthYear:
            monthYear[i] = sorted(monthYear[i], key=month_lookup.index)
        print(monthYear)
    return monthYear


def reteriveDetails(conn,request):
    email = request.form['email']
    month= datetime.strptime(request.form['month'], '%B').month
    year = request.form['year']
    print(email,month,year)
    sql = f"select * from expense where email = '{email}' and month(expensedate) = {month} and year(expensedate) = {year}"
    out = ibm_db.exec_immediate(conn,sql)
    #dictionary = ibm_db.fetch_both(out)
    arr=[]
    # while dictionary != False:
    #     arr.append(dictionary)
    #     dictionary = ibm_db.fetch_row(out) 

    while ibm_db.fetch_row(out) != False:
        date = ibm_db.result(out, 5)
        date = date.strftime('%d-%m-%Y')
        print(ibm_db.result(out, 2), ibm_db.result(out, 3), ibm_db.result(out, 4), ibm_db.result(out, 5))
        arr.append([ibm_db.result(out, 2), ibm_db.result(out, 3), ibm_db.result(out, 4), date])
        #print(ibm_db.result(out, "LASTNAME") )

    print(arr);

    return arr