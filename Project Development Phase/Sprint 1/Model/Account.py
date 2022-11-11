import ibm_db

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
