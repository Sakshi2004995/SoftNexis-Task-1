import pandas as pd
df=pd.read_csv('sample_customer_dataset.csv')
df=df.drop_duplicates()
df['Age']=df['Age'].fillna(df['Age'].median())
df['Salary']=df['Salary'].fillna(df['Salary'].median())
df['City']=df['City'].str.strip().str.title()
df['Name']=df['Name'].str.title()
df.to_csv('cleaned_customer_dataset.csv',index=False)
print('Task Completed Successfully')
