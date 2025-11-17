# define the pandas programing read the  data server

import pandas as pd
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
data=pd.read_csv(url)
print(data.head())