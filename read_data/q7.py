# access the pandas ke throw file form the excel 
import pandas as pd

# read the excel file 
read_data = pd.read_excel("student_data.xlsx")   # quotes lagana zaroori hai
print("Read the excel file data:\n", read_data)
