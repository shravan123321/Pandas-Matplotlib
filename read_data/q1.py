# define the panda and then read the file form the another lucations
import pandas as pd

read = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")  # replace filename.csv with your actual file name
print(read)
