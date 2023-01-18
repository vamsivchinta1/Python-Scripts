```editting cells by columns```
df['B'].str.replace('[^\w\s]', '') # removing special characters but not spaces from cells 
df['A'] = df['A'].div(100).round(2) # dividing cells by int

'''extracting characters from columns'''
df['col2'] = df['col1'].str[-4:] # right()
df['col2'] = df['col1'].str[:5] # left()
df['col2'] = df['col1'].str[3:8] # middle()
df['col2'] = df['col1'].str.split('-').str[0] # Before a symbol
df['col2'] = df['col1'].str.split('-').str[1]
df['col2'] = df['col2'].str.split('$').str[0]

'''row editting'''
df = df.sample(n = 3) # To get 3 random rows
df = df.sample(frac = 0.5) # here you get .50 % of the rows
df.dropna(axis='index', how='any', inplace=True)
df = df.loc[(df["col1"] > 0) & (df["col2"] > 0)] # Deleting rows based on a column value
df = df[df['zip'].notnull()] # Drop rows with None/NaN
df.loc[df['col1'].isin([value1, value2, value3, ...])] # Filtering in rows based on list of col values
df = df.dropna(subset=['colA', 'colC']) # Drop rows where specific column values are null
# using Datetime Package
df[(df['date']>datetime.date(2016,1,1)) & (df['date']<datetime.date(2016,3,1))]  # filtering rows out based on date column


'''list editting'''
list = ['larry', 'curly', 'moe']
list.append('shemp')         ## append elem at end
list.insert(0, 'xxx')        ## insert elem at index 0
list.extend(['yyy', 'zzz'])  ## add list of elems at end

'''MultiIndexing'''
df.set_index(['year', 'month'], inplace=True)
list(mi.columns.levels[0])   | mi = multiindex dataframe

'''Imputting'''
df.fillna('',inplace=True)
df = df.fillna('')
df[col].fillna(0, inplace=True)
df['column_name'] = df['column_name'].replace('-','None')

'''Joining'''
df = pd.merge(df1, df2, on='A', how='inner')
df = pd.concat([df1, df2])

'''Exporting Data'''
df.to_excel('cat_kst_df.xlsx', sheet_name='Sheet_name_1')





'''Column Values Editting'''
data["First Name"]= data["First Name"].str.lower()


'''working with data types'''
# checking data types
print(df.dtypes)
type(a) # id type of object
df = df.apply(pd.to_numeric) # convert dtype of all columns of DataFrame
df[["a", "b"]] = df[["a", "b"]].apply(pd.to_numeric) # convert dtype of just columns "a" and "b"
df['column name'] = df['column name'].astype(np.int64)












'''python libs'''
import pandas as pd
import os

'''misc code:''' 
pd.set_option('display.max_columns', None)
new_directory = os.path.join(currentDirectory, r'NewDirectoryFolderName')
  if not os.path.exists(new_directory):
      os.makedirs(new_directory)

cwd = os.getcwd()
print("Current working directory: {0}".format(cwd))

'''group by'''
df_cal = df_cal.groupby(['Year']).agg(
    date = pd.NamedAgg(column = 'Date', aggfunc=min)
)
      
'''misc. table functions'''
fp = 'C:\Users\vamsi\Aspirent Consulting, LLC\ActiveGraf - General\Analytics Platform Data Warehouse\'
df.to_csv(path = fp,'my_new_file.csv', index=False)
df.shape
