# API_EspPy
 API to save data from esp to a database

-----------------------------------------------

How works:

    *localhost/POST_Output_Staus -> to update the DB with new variables
        
        wait all variables create by the user but the frist column is fixed to ID auto_increment
        
        Output
            JSON{
                "OK"
                }

    *localhost/GET_Output_Staus -> to read the DB waits three fixed values
        
        wait three variables a fix 
       
        Output
            JSON{
                "OK"
                }

    *localhost/PostDBcreate -> to create a new table 
        
        wait to create a new table
            JSON{
                Table : Name
                Column[x] : Type
                Column[x] : Type
                ....
            }

        Output
            JSON{
                "OK"
                }

Use: 

    python
    mariaDB

Improvements

    V200 -> create a Auth system and use HTTPS
    V300 -> improve GET_Output_Staus to have the option to select what columns to read