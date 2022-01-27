import mariadb
import sys

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="UserAutomation",
        password="12D!09b@",
        host="192.168.15.2",
        port=3306,
        database="automationDB"

    )
except mariadb.Error as ex: 

    print(f"An error occurred while connecting to MariaDB: {ex}") 

    sys.exit(1) 



cur = conn.cursor()    

def ConfirmRequestData(data1, data2):
    
    print(data1)
    print(data2)

    #return true


def ReadDB():
    pass


def DBwrite(data):

#    cur.execute("CREATE TABLE output (ID_User VARCHAR(30),ID_Board VARCHAR(30), HASH VARCHAR(30))");

#    cur.execute("INSERT INTO output (ID_User, ID_Board,HASH ) VALUES ('1f51af65d16a5','g56s1g65s', 'fadfdafdas')")
        
  
#   query = f"INSERT INTO PRODUCT (PRODUCT_ID, price,PRODUCT_TYPE) VALUES ('{PRODUCT_ID}', '{price}', '{PRODUCT_TYPE}')"
  #  print(data["ID_User"])

    print(len(data))
    JSON_Keys = data.keys()
    print(data[key])
  
    ID_User1 = data["ID_User"]
    ID_BD1 = data["ID_Board"]
    HASH1 = data["HASH"]
    Output1 = data["ID_Output"]

   # query = f"INSERT INTO output (ID_User ,ID_Board , HASH, ID_Output ) VALUES ('{ID_User1}', '{ID_BD1}','{HASH1}','{Output1}')"
  #  cur.execute(query)

   # conn.commit()