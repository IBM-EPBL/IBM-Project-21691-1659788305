
import ibm_db
try:
    conn=ibm_db.connect("DATABASE=bludb;HOSTNAME=6667d8e9-9d4d-4ccb-ba32-21da3bb5aafc.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=30376;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;PROTOCOL=TCPIP;UID=kmr99620;PWD=LobZeAIWWJi6zOdS;", "", "")
    print("Db connected")
    
except:
    print("Error")

email = 'harish@gmail.com'
password = '12345'
sql =  f"select * from udetails;"
out = ibm_db.exec_immediate(conn,sql)
print(ibm_db.fetch_assoc(out))

