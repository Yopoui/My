import json
import pandas as pd

#with open('students.json', 'r', encoding='utf-8') as f:
#    data = json.load(f)

#df = pd.DataFrame(data['students'])
#df.to_excel('students.xlsx', index=False)

with open('C:/Users/sss/Desktop/json to excel/user.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

df = pd.DataFrame(data['students'])
df.to_excel('C:/Users/sss/Desktop/json to excel/user.xlsx', index=False)