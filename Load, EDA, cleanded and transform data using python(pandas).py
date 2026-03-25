import pandas as pd
df = pd.read_csv(r"e:\Data Sets\Customer Shoping Behavior\customer_shopping_behavior.csv")
#pd.set_option('display.expand_frame_repr',False)
#df=df.head()
#df.info()
#df=df.describe(include='all')
#df=df.isnull().sum()

df['Review Rating'] = df.groupby('Category')['Review Rating'].transform(lambda x: x.fillna(x.median()))
df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ','_')
df.rename(columns= {'purchase_amount_(usd)':'purchase_amount'},inplace=True)

#Creating a column "aged-group"
df['age_group'] = pd.qcut(df['age'], q=4 ,labels=['Young Adult','Adult','Middle-aged','Senior'])

# Create column "purchase_frequency_days"
frequency_mapping = {
    'Fortnightly' : 14,
    'Weekly' : 7,
    'Monthly' : 30,
    'Quarterly' : 90,
    'Bi-Weekly' : 14,
    'Annually' : 365,
    'Every 3 Months' : 90
}
df['purchase_frequency_days'] = df['frequency_of_purchases'].map(frequency_mapping)


df=df.drop('promo_code_used', axis=1)
print(df)
'''
from sqlalchemy import create_engine
engine = create_engine("mysql+mysqlconnector://root:arsalmalik@localhost:3306/customer_behavior")
print('uploading data to mysql, please wait \n')
df.to_sql('customer_shopping_table',engine, index=False, if_exists='replace', method='multi')
print('data is uploaded successfully')
engine.dispose()'''

df.to_csv(r"E:\Data Sets\cleaned_customer_data.csv", index=False)
print('comma separated file is created')