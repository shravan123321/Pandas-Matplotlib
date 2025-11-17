# What is the avrage paid by people who survied
import pandas as pd
#defien the database 
data1 = {
    'A': [1, 2, 3, None, 5, None, None, 8, None, 10],
    'B': [None, 12, None, None, None, None, 17, 18, 19, 20]
}

dbase=pd.DataFrame(data1)

sur=dbase[dbase.surived==1]['fare']
print(sur)