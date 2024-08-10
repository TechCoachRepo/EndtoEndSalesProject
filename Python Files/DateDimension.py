# import pandas library 
import pandas as pd 


# start date and end date between which we need to geenrate our dates 

start_date ='2014-01-01'
end_date='2024-12-31'

# generate a series of dates between the start and the end date 

date_range=pd.date_range(start=start_date, end = end_date)

# convert these series of dates into a data frame 

date_dimension = pd.DataFrame(date_range,columns = ['Date'])


# add new columns to our dataframe DayofWeek Month Quarter Year Isweekend DateID
date_dimension['DayofWeek'] = date_dimension['Date'].dt.dayofweek
date_dimension['Month'] = date_dimension['Date'].dt.month
date_dimension['Quarter'] = date_dimension['Date'].dt.quarter
date_dimension['Year'] = date_dimension['Date'].dt.year
date_dimension['Isweekend'] = date_dimension['DayofWeek'].isin([5,6])
date_dimension['DateID'] = date_dimension['Date'].dt.strftime('%Y%m%d').astype(int)

# reorder our data frame so that the dateid becomes the 1st column

cols = ['DateID'] + [col for col in date_dimension.columns if col != 'DateID']
date_dimension=date_dimension[cols]



# export it into a csv index column to be ignored 
date_dimension.to_csv('DimDate.csv',index=False)