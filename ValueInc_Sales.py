# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 20:51:18 2022

@author: kanie
"""

import pandas as pd

# file_name = pd.read_csv("file.csv") < ---- format of read_csv

data = pd.read_csv("transaction.csv")

data = pd.read_csv("transaction.csv", sep=";")

# Summary of our data
data.info()

#working with calculations
#Defining variables

CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberOfItemsPurchased = 6

#Mathematical Operation on Tableau

ProfitPerItem = 21.11 - 11.73
ProfitPerItem = SellingPricePerItem - CostPerItem

ProfitPerTransaction = NumberOfItemsPurchased * ProfitPerItem
CostPerTransaction = NumberOfItemsPurchased * CostPerItem
SellingPricePerTransaction = NumberOfItemsPurchased * SellingPricePerItem

#Cost Per Transaction column calculation
#CostPerTransaction = NumberOfItemsPurchased * CostPerItem
#To single out columns: variable = dataframe['column_name']

CostPerItem = data['CostPerItem']
NumberOfItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberOfItemsPurchased

#Adding a new column to a dataframe

data['CostPerTransaction'] = CostPerTransaction
#or

data['CostPerTransaction'] = data['CostPerItem'] * data['NumberOfItemsPurchased']

#sales Per Transactions

data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

#Profit Calculation = Sales - Cost
data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

#Markup = (Sales - Cost) / Cost
data['Markup'] = (data['SalesPerTransaction'] - data['CostPerTransaction']) / data['CostPerTransaction']

#Rounding Markup 
roundmarkup = round(data['Markup'], 2)

data['Markup'] = round(data['Markup'], 2)

#Combining data fields / columns

my_name = 'Kanwulia' + 'Iyamu'
my_date = "Day"+"-"+"Month"+"-"+"Year"

#checking columns data type
print(data['Day'].dtype)

#change columns type
day = data['Day'].astype(str)
year = data['Year'].astype(str)
print(day.dtype)
print(year.dtype)



my_date = day+'-'+data['Month']+'-' + year

data['date'] = my_date

#Using iloc to view specific columns/rows from Pandas
data.iloc[0]       #views the rows with index = 0. index starts counting from 0
data.iloc[0:3]     #first 3 rows
data.iloc[-5:]      #last 5 rows
data.head(5)       #brings in first 5 rows

data.iloc[:,2]    # brings in all rows from column index 2 i.e. 3rd column
data.iloc[4,2]    #brings in 4th row from column index 2

#using split to split the client keywords field
#new_var = column.str.split('sep' , expand = True)

split_col = data['ClientKeywords'].str.split(',' , expand = True)

#Creating new columns for the split columns in Client Keywords

data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthOfContract'] = split_col[2]


#using the replace function
data['ClientAge'] = data['ClientAge'].str.replace('[' , '')
data['LengthOfContract'] = data['LengthOfContract'].str.replace(']' , '')

#using the lower function to change item to lowercase

data['ItemDescription'] = data['ItemDescription'].str.lower()

#how to merge files
#bringing in a new dataset

seasons = pd.read_csv('value_inc_seasons.csv' , sep = ';')

#merging files: merge_df = pd.merge(df_old, df_new, on = 'key')
data = pd.merge(data, seasons, on = 'Month')

#dropping columns
# df = df.drop('columnname' , axis = 1)
data = data.drop('ClientKeywords' , axis = 1)
data = data.drop('Day' , axis = 1)
data = data.drop(['Month', 'Year'] , axis = 1)

#Export to a CSV
data.to_csv('ValueInc_Cleaned.csv', index = False)

