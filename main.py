import mariadb
import sys
import os

# Login information
user1 = os.environ.get('DB_Automation_User')
password1 = os.environ.get('DB_Automation_PASSWD')

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user = user1,
        password = password1,
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


def DBwrite(DataInput):

#    cur.execute("CREATE TABLE output (ID_User VARCHAR(30),ID_Board VARCHAR(30), HASH VARCHAR(30))");

#    cur.execute("INSERT INTO output (ID_User, ID_Board,HASH ) VALUES ('1f51af65d16a5','g56s1g65s', 'fadfdafdas')")
        
  
#   query = f"INSERT INTO PRODUCT (PRODUCT_ID, price,PRODUCT_TYPE) VALUES ('{PRODUCT_ID}', '{price}', '{PRODUCT_TYPE}')"
  #  print(data["ID_User"])

    print(len(DataInput))
    JSON_Keys = DataInput.keys()


    print(type(JSON_Keys))

    DataInputKeys = list()
    for i in DataInput.keys():
        DataInputKeys.append(i)

    print(DataInputKeys[1])

    #query = 
  
    ID_User1 = DataInput["ID_User"]
    ID_BD1 = DataInput["ID_Board"]
    HASH1 = DataInput["HASH"]
    Output1 = DataInput["ID_Output"]



   # query = f"INSERT INTO output (ID_User ,ID_Board , HASH, ID_Output ) VALUES ('{ID_User1}', '{ID_BD1}','{HASH1}','{Output1}')"
  #  cur.execute(query)

   # conn.commit()