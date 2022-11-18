import ibm_db

def connect():
    conn = None
    try:
        conn=ibm_db.connect("DATABASE=bludb;HOSTNAME=6667d8e9-9d4d-4ccb-ba32-21da3bb5aafc.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=30376;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;PROTOCOL=TCPIP;UID=kmr99620;PWD=LobZeAIWWJi6zOdS;", "", "")
        print("Db connected")

    except Exception as e:
        print(e)
    return conn