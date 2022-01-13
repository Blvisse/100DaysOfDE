import mysql.connector as mysql
import sys
import pandas as pd

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
cursor=connection.cursor(buffered=True)

try:
    data=pd.read_csv('../data/date_data.csv')
    print("Successfully read data file")
    print(data.head())

except Exception as e:
    print ("Error: " ,e)
    sys.exit(1)
    
for i,row in data.iterrows():
    try:
        query='''
        INSERT INTO DEMO3.EMPLOYEES_DATA(NAME,EMAIL,PHONE,ADDRESS,DATE_JOINED) VALUES ( %s, %s, %s, %s,%s)
        '''
        
        cursor.execute(query,tuple(row))
        connection.commit()
        
    except Exception as e:
        print("skipping data: ",row)
        print("Error: ",e)
        sys.exit(1)
    
print("Data inserted successfully")