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


# Get Cursor 

cur = conn.cursor()
sql1 =  ''' CREATE TABLE output(
ID INT KEY NOT NULL AUTO_INCREMENT ,
ID_User VARCHAR(30),
ID_Board VARCHAR(30),
HASH VARCHAR(30) UNIQUE KEY,
ID_Output TINYINT
)'''


sql2 = "CREATE TABLE `employees` ("
"  `emp_no` int(11) NOT NULL AUTO_INCREMENT,"
"  `birth_date` date NOT NULL,"
"  `first_name` varchar(14) NOT NULL,"
"  `last_name` varchar(16) NOT NULL,"
"  `gender` enum('M','F') NOT NULL,"
"  `hire_date` date NOT NULL,"
"  PRIMARY KEY (`emp_no`)"
") ENGINE=InnoDB"




#cur.execute("CREATE TABLE output (ID TINYINT unsigned NOT NULL AUTO_INCREMENT ,ID_User VARCHAR(30),ID_Board VARCHAR(30), HASH VARCHAR(30) UNIQUE ,ID_Output TINYINT, Time smalldatetime)");
#cur.execute(sql1)
#cur.execute("ALTER TABLE output(Teste INT)")

#cur.execute("INSERT INTO output (ID_User, ID_Board,HASH ) VALUES ('1f51af65d16a5','g56s1g65s', 'fadfdafdas')")

conn.commit()



#   ID_User
#   ID_Board
#   HASH
#   Outputs