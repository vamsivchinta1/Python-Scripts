# column editting
```python
df1 = df[['a','b']]
df.loc[:, ['food', 'color']]
df1 = df.iloc[:,0:2]

df.loc[:, df.columns != 'b']
df = df[df.columns.difference(['target_col'])]
df.drop(['a', 'b'], axis=1)

col_names = ['nnn', 'mmm', 'yyy', 'zzzzzz']
df.loc[:, df.columns.isin(col_names)] # filtering in columns by list of column names

df.loc[:, df.columns.str.contains('Estimate')] # filtering In column names that contain a certain string
or
df.filter(like='Estimate')

df = df.loc[:, ~df.columns.str.contains('Margin')] # filtering out column names that contain a certain string
```

# needs to be re-arranged
```python
print(df['col'].unique()) # list of unique column values
```
```python
df['new_column'] = np.where(df['col2']<9, 'value1',
                   np.where(df['col2']<12, 'value2',
                   np.where(df['col2']<15, 'value3', 'value4')))
```
```python
df1['Age Group'].unique()
df1 = df1.sort_values(by=['Date','LICENSE NUMBER'])
data.rename(columns={'gdp':'log(gdp)'}, inplace=True) # rename one column name
```
