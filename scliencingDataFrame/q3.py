# define the data file and then so file backoudfill file 
import pandas as pd
#defien the database 
data1 = {
    'A': [1, 2, 3, None, 5, None, None, 8, None, 10],
    'B': [None, 12, None, None, None, None, 17, 18, 19, 20]
}

# Store the data the da1
da1=pd.DataFrame(data1)
da2=da1.fillna(method="bfill") # data Store the null valu in backoud fill
print("original data:\n",da2)