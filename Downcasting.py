
'''
This is a fairly decent example of downcasting
Downcasting is the process of casting a type to a lower type
For example int64 to in32 or most common float64 to float32

This can be very useful when memory space is of concern (this is fairly common)
THis will allow you to change the type of the variables to a smaller type which saves on space
Further this is good practice in general, if you don't need 64 bytes of information don't keep the field as that
'''

import pandas as pd
df = pd.DataFrame()

'''
assume your data is in a pandas dataframe df
the way to check the amount of memory df is using the info method
also you can select type using the select_dtypes method
'''

df.info(memory='deep') #gives you a detailed readout of memory usage
#Note that specifying memory='deep' gives you a readout of all the fields in the dataset

df.select_dtypes(include=['pass type you want here'])

'''
Now lets look at downcasting various dtypes
'''

#Downcasting int64 example
data_int = df.select_dtypes(include = ['int64'])
downcasted_int = data_int.apply(pd.to_numeric, downcast='unsigned')

#Downcasting float
data_float = df.select_dtypes(include = ['float'])
downcasted_float = data_int.apply(pd.to_numeric, downcast='float')

#you can downcast dates but thats probably not really useful
#Rather just pull them out

data_dates = df.select_dtypes(include = ['datetime'])

#Object types are a little bit more involved
data_obj = df.select_dtypes(include = ['object'])
downcasted_object = pd.DataFrame() #initialize an empty dataframe

for col in data_obj.columns:
    num_unique_values = len(data_obj[col].unique())
    num_total_values = len(data_obj[col])
    if num_unique_values / num_total_values < 0.5:
        downcasted_object.loc[:, col] = data_obj[col].astype('category')
    else:
        downcasted_object.loc[:, col] = data_obj[col]

'''
Then you can put the dataset back together again in whatever way you want
Here are two ways
'''

#Way One the simple way
#Just put the data back together based on type
optimized_data = pd.concat([downcasted_int,
                           downcasted_float,
                           downcasted_object,
                           data_dates],
                           axis=1)

#Way Two slightly better
#Puts the dataset back in the original order

col_order = list(df.columns)
concat_data = pd.concat([downcasted_int,
                        downcasted_float,
                        downcasted_object,
                        data_dates],
                        axis=1)
optimized_data = concat_data[col_order]


'''
If for some reason you need to save this for use on further data pulls
It is super easy to save these to a dictionary for later use
'''

dtypes = optimized_data.select_dtypes(exclude=['datetime']).dtypes
dtypes_col = dtypes.index
dtypes_type = [i.name for i in dtypes.values]
column_types = dict(zip(dtypes_col, dtypes_type))
