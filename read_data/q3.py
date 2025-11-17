# Check the Panda data structure
import pandas as pd

data = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

print("types: ", type(data))
print("Age type: ", type(data["Age"]))

l = [1, 2, 3, 4, 5]
# checking the series of list 
ser = pd.Series(l)
print("Series of list:---\n", ser)
print("types of series:\n", type(pd.Series(l)))
