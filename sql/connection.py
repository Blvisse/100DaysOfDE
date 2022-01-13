'''

This script tests connection to the mysql database using a python connector 

'''

import mysql.connector as mysql
import sys
import os

print("Successfully imported libraries")


try:
    connection=mysql.connect(host="localhost",user="root",password="root")
    print("Connection to mysql db successful")
    print(connection)
except Exception as e:
    print("Connection to mysql db failed")
    print(e)
    sys.exit(1)
    