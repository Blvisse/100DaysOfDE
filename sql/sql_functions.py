'''
This script implements sql functions for our database

'''

import mysql.connector as mysql
import sys


def connection_to_server():    
    connection= None
    try:
        connection=mysql.connect(host="localhost",user="root",password="root", database="DEMO3")
        print("Connection to mysql db successful")
        print(connection)
        
    except Exception as e:
        print("Connection to mysql db failed")
        print(e)
        sys.exit(1)
    return connection

connection=connection_to_server()
cursor=connection.cursor(buffered=True)

#create our first function that calculates duration of an employees contract

query='''

CREATE FUNCTION YEARS(DATE_JOINED DATE) RETURNS INT DETERMINISTIC

BEGIN
    DECLARE current_day DATE;
    SELECT current_date() into current_day;
    RETURN (YEAR(current_day) - YEAR(DATE_JOINED));
    
END



'''

cursor.execute(query)

#we create a new function that determines whether the user deserves a raise according to the number of years served 

query='''

CREATE FUNCTION RAISE(YEARS_SERVED INT) RETURNS BOOLEAN DETERMINISTIC

BEGIN
    DECLARE threshold INT;
    DECLARE result BOOLEAN;
    SET threshold = 10;
    IF YEARS_SERVED >= threshold THEN
    
        SET result=TRUE;
    
    ELSE
    
        SET result=FALSE;
    
    END IF;
    
    RETURN result;
    
    
   
END 
'''

cursor.execute(query)

#now we implement the function on to our table and create a view from it

query='''

CREATE VIEW RAISE AS 
SELECT * ,YEARS(DATE_JOINED) as 'YEARS', RAISE(YEARS(DATE_JOINED)) as 'RAISE'  
FROM EMPLOYEES_DATA

'''
try:
    cursor.execute(query)
    print("Successfully executed query")
    cursor.execute("SELECT * FROM YEARS")
    print(cursor.fetchall())

except Exception as e:
    print("Failed to execute query")
    print(e)
    sys.exit(1)
    
