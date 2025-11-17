# define the pandas code and then file access fill  the excell
import pandas as pd

# data create karte hain
data = {
    "Name": ["Raja","Sanjay", "Ravi", "shravan", "Sudhir"],
    "Age": [23,20, 25, 22, 24],
    "City": ["Delhi","jaipur", "Lucknow", "Patna", "Kanpur"]
}

# DataFrame banate hain
df = pd.DataFrame(data)
print("original data:\n",df)

# Excel file me save karte hain
df.to_excel("student_data.xlsx", index=True)

print("✅ Excel file 'student_data.xlsx' successfully created!")

# da=df[0:6:2]
# print("data viwes:\n ",da)