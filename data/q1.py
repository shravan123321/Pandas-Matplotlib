#define the pandas and data implements null value featching the 
import pandas as pd
data1 = {
    'A': [1, 2, 3, None, 5, None, None, 8, None, 10],
    'B': [None, 12, None, None, None, None, 17, 18, 19, 20]
}
dat=pd.DataFrame(data1)
data=dat.A.fillna("shravan")
print("Data is viewing:\n",data)