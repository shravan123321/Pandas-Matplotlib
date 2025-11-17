#How will make the pandas database new column

import pandas as pd
'''
#1
l=[1,2,3,4,5]
data=pd.DataFrame({'number':[1,2,3,4,5]}) #create the dataframe
print("old data:\n ",data)
#Add the new Column
data['name']="shravan yadav"
print("Modify the data:\n",data)
'''

#2
# create a Series with custom index
data=pd.Series([1,2,3,4],index=[100,"sanjay",3.2,"r"])
print("New dataBase User Modify the (Index and Data)\n",data)

#Convert the Series to dataFrame
dataframe=pd.DataFrame(data)
print("conver the series to dataframe:\n ",dataframe)

#Ager hum index reset karna chahte hai tab
reset=data.reset_index()
print("reset the index:\n",reset)
#delete the particular induvisual index and then compiler showing the new  index line by line row  form me
resert=data.reset_index(drop=True)
print("Full index by data Deleted:\n",resert)
# Edit the column value
ed1=data['name']="Ajay"
ed2=data['age']=20
print("After Modify the data: \n",data)

# removed the datafrome index and number print
re=data.reset_index(drop=True)
print("removed the index data and number print:\n",re)