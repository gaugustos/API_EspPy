#!/usr/bin/python3

from lib2to3.pgen2.token import LESSEQUAL
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




tesadte ="kfkdsjgoijs"

#cur.execute(f"ALTER TABLE AutomationProject ADD ({tesadte}) varchar(40)";)


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


# Get only the JSON keys and transfor to a list    
    #print(len(DataInput))
    JSON_Keys = DataInput.keys()
    #print(type(JSON_Keys))
    DataInputKeys = list()
    for i in DataInput.keys():
        DataInputKeys.append(i)

    print(DataInputKeys)


#get all title columns
    cur.execute("select * from AutomationProject")
    result = cur.fetchall()
    ColumsNames = [i[0] #put in ColumnsNames as cur.description with is the 0 possicion for every place
    for i in cur.description
    ]

    print(ColumsNames)

    DB_Data = {}

    for index in range (len(DataInputKeys)+1):

        if DataInputKeys[index] == ColumsNames[index + 1]:

            DB_Data.update([( DataInputKeys[index] ,'"' + DataInput[DataInputKeys[index]] + '"' )])

            print(index)
            
        elif DataInputKeys[index] !=" ColumsNames[index + 1]":
            
            print("index")
            print(index)
            print(DataInputKeys[index])

            #cur.execute(f"ALTER TABLE AutomationProject ADD {DataInputKeys[index]} VARCHAR(100) NOT NULL")
            #conn.commit()
            
            DB_Data.update([( DataInputKeys[index] ,'"' + DataInput[DataInputKeys[index]] + '"' )])
            
        
    query = f"INSERT INTO AutomationProject ({list(DB_Data.keys())}) VALUES ({(list(DB_Data.values()))})"
    
    # Cleaning the striging for match the MySQL  standard
    query1 = (query.replace("'" ,""))
    query2 = (query1.replace("[" ,""))     
    query3 = (query2.replace("]" ,""))     

    cur.execute(query3)
    conn.commit()

