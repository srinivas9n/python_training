import mysql.connector as connector

import pandas as pd

connection = connector.connect(user='root', password='root', host='localhost', database='world')
cursor = connection.cursor()
query = 'select * from city limit 10'
cursor.execute(query)
results = cursor.fetchall()
data_list = []
for each in results:
    data = {"id": each[0], "name": each[1], "country": each[2], "district": each[3], "population": each[4]}
    data_list.append(data)
df = pd.DataFrame(data_list)
df.to_csv('city.csv', index=False)
