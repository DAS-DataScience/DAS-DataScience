


### Using Pydoc and Cursor

import pydoc

conn = pydoc.connection('Driver={SQL Server};'
                        'Server=  ;'
                        'Trusted_Connection=yes;'
                        'database=     ;'
                        )

cursor = conn.cursor()
cursor.exectute("put sql query here")
data = cursor.fetchall()

for row in data:
    print(row[i])

#Get the columns from the cursor object
#Use the description method

data.cursor_description

#example
print(data[0].cursor_description)
print(data[0].cursor_description[0][0])

columns = []
for i in range(len(data[0].cursor_description)):
    columns.append(data[0].cursor_description[i][0])


### Using Pydoc and Pandas

import pydoc
import pandas as pd

conn = pydoc.connection('Driver={SQL Server};'
                        'Server=  ;'
                        'Trusted_COnnection=yes;'
                        'database=     ;'
                        )

data = pd.read_sql("put sql query here", conn)

'''
*****Note******
If you want to read create a query and read in only last table then:


SET NOCOUNT ON 

WRITE QUERY HERE

select * from whatever the last temp table is

'''


### Using SQL Alchemy and pandas

import pandas as pd
import sqlalchemy as sa
import urllib
params = urllib.parse.quaote_plus('Driver={SQL Server};'
                                   'Server=  ;'
                                   'Trusted_COnnection=yes;'
                                    'database=     ;'
                                  )

enqine = sa.create_engine('mssql+pydoc:///?odbc_connect={}'.format(params))


# Importing table to SQL Server
pd._to_sql(name=' ',
           schema=' ',
           con=engine,
           if_exist='replace',
           method='multi',
           chunksize=    ,
           index=False
           )