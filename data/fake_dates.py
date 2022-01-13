import pandas as pd
import numpy as np
from faker import Faker

print ("Successfully imported libraries")

faker=Faker()

try:
    data=pd.read_csv('data.csv')
    print("Successfully read data file")
    print(data)
except Exception as e:
    print ("Error: " ,e)
    
    
data.dropna(inplace=True,axis=0)
print(data)
Faker.seed(0)

#generate fake dates between 1/1/1997 and 1/1/2020

data['Date_of_registration']=[ faker.date_between(start_date="-25y", end_date="today") for i in range(len(data))]
    

print(data)


#save the data into a new csv file
data.to_csv('date_data.csv',index=False)
print("Saved to CSV file")
