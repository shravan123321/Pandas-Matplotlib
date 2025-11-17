# define the another lucation file showing the data form column
import pandas as pd

data=pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

print("data: ",data)
col=data.columns
print("data file column: ",col)


'''
# check the type of data 
ty=data.dtypes
print("data types: ",ty)


# first five data row access
top=data.head()
print("top data: \n",top)

#last five data row pprint 
last=data.tail()
print("last five data: \n",last)

# mid data row access five
mid=data.sample(5) #numbering jitna dene se autna hi data access hota hai ager hum 5 diye hai to five hi data access hoga
print("mid five data: \n",mid)


# define the statical information about numerical column
num=data.describe()
print(num)
'''
# Total view the null value
nul=data.isnull().sum()
print("null value:\n",nul)
# print("view the all data form structure:\n",data)
 