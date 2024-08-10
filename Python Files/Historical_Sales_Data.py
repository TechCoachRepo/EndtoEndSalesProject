import pandas as pd
import numpy as np


num_rows = int(input(" Enter the number of rows for orders : "))

#generate the series of dates between 2014 and 2024 

random_dates = np.random.choice(np.arange(np.datetime64('2014-01-01'),np.datetime64('2024-07-28')),size = num_rows)


formatted_rows = pd.to_datetime(random_dates).strftime('%Y%m%d')


data = {
    'DateID': formatted_rows,
    'ProductID': np.random.randint(1,1001,size=num_rows),
    'StoreID': np.random.randint(1,101,size=num_rows),
    'CustomerID': np.random.randint(1,1001,size=num_rows),
    'QuantityOrderded': np.random.randint(1,21,size=num_rows),   
    'OrderAmount': np.random.randint(100,1001,size=num_rows)
    }
    


df = pd.DataFrame(data)


discount_perc = np.random.uniform(0.02,0.15,size=num_rows)
shipping_cost = np.random.uniform(0.05,0.15,size=num_rows)


# calculate columns 

df['DiscountAmount'] = df['OrderAmount'] * discount_perc
df['Shipping Cost'] = df['OrderAmount'] * shipping_cost
df['TotalAmount'] = df['OrderAmount'] -(df['DiscountAmount']+df['Shipping Cost'])
print(df)

df.to_csv('factorders.csv',index=False)


""" These are the column we need to generate 
'DateID' -- random date in a date range in a specified format 
'ProductID' -- random 
'StoreID' -- random 
'CustomerID' -- random 
'QuantityOrderded' -- random 
'OrderAmount' -- random 
'DiscountAmount' -- Calculated dependent on OrderAmount
'Shipping Cost' -- Calculated dependent on OrderAmount
'TotalAmount' -- Calculated dependent on OrderAmount and others  
"""

