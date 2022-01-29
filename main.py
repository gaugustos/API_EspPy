#!/usr/bin/python3

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


def ReadDB(Data):

    
    DataInputvalues = list()
    for i in Data.values():
        DataInputvalues.append(i)

    DBOutput ={}
    DBOutputKey = list()

    DBOutputKey = ["ID_Output", "Value_Sensor_1", "Value_Sensor_2", "Value_Sensor_3", "Last_Update"]

    query = f"SELECT ID_Output, Value_Sensor_1, Value_Sensor_2, Value_Sensor_3, Last_Update FROM AutomationProject WHERE ID_User= '{DataInputvalues[0]}' and ID_Board= '{DataInputvalues[1]}' and ID_HASH= '{DataInputvalues[2]}';"
   
   
    cur.execute(query)
    
    for (DBOutputKey) in cur:
        DBOutput = DBOutputKey
    
    return DBOutput

def DBwrite(DataInput):


# Get only the JSON keys and transfor to a list    
    JSON_Keys = DataInput.keys()
   
    DataInputKeys = list()
    for i in DataInput.keys():
        DataInputKeys.append(i)

   

    #get all title columns
    cur.execute("select * from AutomationProject")
    ColumsNames = [i[0] #put in ColumnsNames as cur.description with is the 0 possicion for every place
    for i in cur.description
    ]


    DB_Data = {}

    for index in range (len(DataInputKeys)):

        if DataInputKeys[index] == ColumsNames[index + 1]:

            DB_Data.update([( DataInputKeys[index] ,'"' + DataInput[DataInputKeys[index]] + '"' )])
            
      #  else: # DataInputKeys[index] != ColumsNames[index + 1]:


    query = f"INSERT INTO AutomationProject ({list(DB_Data.keys())}) VALUES ({(list(DB_Data.values()))})";
    
    # Cleaning the striging for match the MySQL  standard
    query1 =(query.replace("'" ,""))
    query2 = (query1.replace("[" ,""))     
    query3 = (query2.replace("]" ,""))     

    cur.execute(query3)
    conn.commit()



def DBcreate(DataInput):
   
    DataInputValue = list()
    for i in DataInput.values():
        DataInputValue.append(i)

    DataInputKeys = list()
    for x in DataInput.keys():
        DataInputKeys.append(x)

    query1 = list()

    for i in range(1 ,len(DataInput)):

        query1.append(f"{DataInputKeys[i]} {DataInputValue[i]}")

    CleanText = CleanDB_String(query1)
    
    query = f"CREATE TABLE {DataInputValue[0]} ({CleanText})"

    #query = "CREATE TABLE dsadadffhhkjjk"
    print(query)
    cur.execute(query)
   
    conn.commit()

    
def CleanDB_String(TEXT):
    
    string  = " ".join(TEXT)

    return string  