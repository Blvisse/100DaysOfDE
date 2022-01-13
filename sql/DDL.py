'''
This script tests SQL Data Definition Language (DDL) statements

'''

import mysql.connector as mysql

import sys

#create a connection to the database

def connection_to_server():    
    connection= None
    try:
        connection=mysql.connect(host="localhost",user="root",password="root")
        print("Connection to mysql db successful")
        print(connection)
        
    except Exception as e:
        print("Connection to mysql db failed")
        print(e)
        sys.exit(1)
    return connection

connection=connection_to_server()
        

def create_db(query):
    
    try:
        cursor.execute(query)
        print("Database created successfully")
        cursor.execute("SHOW DATABASES")
        print(cursor.fetchall())
    except Exception as e:
        print ("Failed to create database")
        print("Error: " + e.message)
    
def run_query(query):
    try:
        cursor.execute(query)
        print("Query run successfully")
        # print(cursor.fetchall())
    except Exception as e:
        print ("Failed to run query")
        print(f"Error: {e}".format(e))
    
    
#create a cursor object
cursor=connection.cursor(buffered=True)


'''
The SQL statents categorized as DDL statements are:
1. CREATE
2. DROP
3. ALTER
4.TRUNCATE
5. COMMENT
6. RENAME

'''

#CREATE DDL statements

query='''CREATE DATABASE IF NOT EXISTS DEMO '''

try:
    cursor.execute(query)
    print("Database created successfully")
    cursor.execute("SHOW DATABASES")
    print(cursor.fetchall())
except Exception as e:
    print ("Failed to create database")
    print("Error: " + e.message)

#DROP DDL statements
#we create a second table and then drop it
query='''CREATE DATABASE IF NOT EXISTS DEMO2 '''

try:
    cursor.execute(query)
    print("Database created successfully")
    cursor.execute("SHOW DATABASES")
    
    dbs=cursor.fetchall()
    print("Databases found in the server are: ")
    for db in dbs:
        print("Database name: ",db)
except Exception as e:
    print ("Failed to create database")
    print("Error: " + e.message)
    
query='''DROP DATABASE IF EXISTS DEMO2 '''
try:
    cursor.execute(query)
    print("Database DEMO2 successfully deleted")
except Exception as e:
    print ("Failed to drop database")
    print("Error: " + e.message)


'''

ALTER DDL statements
we create a new database and then alter its read only property

'''

query='''CREATE DATABASE IF NOT EXISTS DEMO3 '''

create_db(query)


# we first read our database property
query='''SELECT * FROM INFORMATION_SCHEMA.SCHEMA_PROPERTIES WHERE SCHEMA_NAME = 'DEMO3' AND PROPERTY_NAME = 'DEFAULT_CHARACTER_SET_NAME' '''
query3=''' SHOW CREATE DATABASE DEMO3'''
cursor.execute(query3)
print("Our created database DEMO3 has the following properties: ")
print(cursor.fetchall())


#since we do see our db is readonly, we alter it to be writable

query = ''' ALTER DATABASE DEMO3 READ ONLY =1 '''
run_query(query)
print("Database DEMO3 successfully altered")

#now we check our properties again
cursor.execute(query3)
print("Our created database DEMO3 has the following properties: ")
print(cursor.fetchall())



'''

We can also use DDL statements to create tables or manipulate database objects such as tables, views, stored procedures, triggers, etc.

'''

#CREATE TABLE
query='''CREATE TABLE IF NOT EXISTS DEMO3.EMPLOYEE (NAME VARCHAR(255) NOT NULL, ID INTEGER PRIMARY KEY, GENDER CHAR(1), JOIN_DATE DATE ); '''
cursor.execute(query)
cursor.execute("USE DEMO3")
cursor.execute("SHOW TABLES")
print("The tables listed in the database are: {} ".format(cursor.fetchall()))


#create a new table where we shall store our data
query= ''' 

CREATE TABLE IF NOT EXISTS DEMO3.EMPLOYEES_DATA ( 
ID INTEGER AUTO_INCREMENT PRIMARY KEY, 
NAME VARCHAR(255) NOT NULL, 
EMAIL VARCHAR(255) NOT NULL, 
PHONE VARCHAR(255) NOT NULL, 
ADDRESS VARCHAR(255) NOT NULL,
DATE_JOINED DATE NOT NULL);

'''
cursor.execute(query)
cursor.execute("SHOW TABLES")


#we create a view of the table in our db
def create_view(view_name: str,table_name: str):
    
    '''
    
    This function is used to create a view of a table
    
    return: View created successfully
    '''
    query = ''' CREATE VIEW {} AS 
    SELECT NAME,PHONE 
    FROM {} 
    
    '''.format(view_name,table_name)

    cursor.execute(query)
    
    cursor.execute("SELECT * FROM {}".format(view_name))
    print(cursor.fetchall())
    
create_view(view_name="EMPLOYEEs_VIEW",table_name="EMPLOYEES_DATA")


