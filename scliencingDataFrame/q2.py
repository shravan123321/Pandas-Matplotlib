# define the data file and then so forward file 
import pandas as pd

data1 = {
    'A': [1, 2, 3, None, 5, None, None, 8, None, 10],
    'B': [None, 12, None, None, None, None, 17, 18, 19, 20]
}

da = pd.DataFrame(data1)

# fillna method (forward fill)
da2 = da.fillna(method='ffill')
print("methods add the:\n", da2)
