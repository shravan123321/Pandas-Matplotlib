# Access the data particular format me
import pandas as pd
data1 = {
    'A': [1, 2, 3, None, 5, None, None, 8, None, 10],
    'B': [None, 12, None, None, None, None, 17, 18, 19, 20]
}
dat=pd.DataFrame(data1)
# Change the Null value form the data
dl=dat.fillna("shravan")
print("all the data value should be change the:\n",dl)
