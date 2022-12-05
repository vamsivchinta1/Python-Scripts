'''Column Header Editting'''
print(df.columns.values.tolist())
df.columns = df.columns.str.upper()
df.columns = df.columns.str.lower()
df.columns = df.columns.str.title() #camel casing
df.columns = df.columns.str.strip() #to remove all the leading or trailing spaces
df.columns = df.columns.map(lambda x : x.replace("-", "_").replace(" ", "_")) #a simple lambda function to replace the space and hyphen with underscore
dict = {'Dept.1':'Dept','Class.1':'Class'}
df1.rename(columns=dict, inplace=True)
df = df[['Year'] + [ col for col in df.columns if col != 'Year' ] ] # moving column to first position of a df

'''column editting'''
df1['Age Group'].unique()
df1 = df1.sort_values(by=['Date','LICENSE NUMBER'])
data.rename(columns={'gdp':'log(gdp)'}, inplace=True) # rename one column name
df1 = df[['a','b']]
df.loc[:, ['food', 'color']]
df1 = df.iloc[:,0:2]

print(df['col'].unique()) # list of unique column values
df.loc[:, df.columns != 'b']
df = df[df.columns.difference(['target_col'])]
df.drop(['a', 'b'], axis=1)

df['new_column'] = np.where(df['col2']<9, 'value1',
                   np.where(df['col2']<12, 'value2',
                   np.where(df['col2']<15, 'value3', 'value4')))

col_names = ['nnn', 'mmm', 'yyy', 'zzzzzz']
df.loc[:, df.columns.isin(col_names)] # filtering in columns by list of column names

df.loc[:, df.columns.str.contains('Estimate')] # filtering In column names that contain a certain string
or
df.filter(like='Estimate')

df = df.loc[:, ~df.columns.str.contains('Margin')] # filtering out column names that contain a certain string



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


'''Working w/ Dates'''
df2['Date'] = pd.to_datetime(df.Year, format='%Y') #convert year column to date
df['datetime'] = pd.to_datetime(df['datetime']).dt.date
df['year'] = pd.DatetimeIndex(df['birth_date']).year #extracting year from date col



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


      
'''misc. table functions'''
fp = 'C:\Users\vamsi\Aspirent Consulting, LLC\ActiveGraf - General\Analytics Platform Data Warehouse\'
df.to_csv(path = fp,'my_new_file.csv', index=False)
df.shape
