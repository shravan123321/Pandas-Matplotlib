# define the DataFrame
import pandas as pd

data1 = {
    'A': [1, 2, 3, None, 4, None, None, 7, None, 8, None, None],
    'B': [None, 12, None, None, None, None, 17, 18, 19, 20, None, None]
}

data = pd.DataFrame(data1)
# print("Data is:\n", data)
# da=data.A.fillna(0)
# print(da)
