# define the pandas and visualize data in proper format
import pandas as pd

# data create with column format
data = pd.DataFrame({
    "name": ["sanjay", "ravi", "amit"],
    "age": [23, 25, 22]
})

print("Old data:\n", data)

# add new column
data["new_name"] = ["sudhir yadav", "rahul verma", "deepak"]
data["new_age"] = ["guess the age", "guess the age", "guess the age"]

print("\nModified data:\n", data)
