# Column Header Editting
Viewing Column Headers
```python
print(df.columns.values.tolist())
```
Renaming Column Headers
```python
dict = {'Dept.1':'Dept','Class.1':'Class'}
df1.rename(columns=dict, inplace=True)
```
Formatting Column Headers
```python
df.columns = df.columns.str.upper()
df.columns = df.columns.str.lower()
df.columns = df.columns.str.title() #camel casing
df.columns = df.columns.str.strip() #to remove all the leading or trailing spaces
df.columns = df.columns.map(lambda x : x.replace("-", "_").replace(" ", "_")) #a simple lambda function to replace the space and hyphen with underscore
```
Rearranging Column Headers
```python
df = df[['Year'] + [ col for col in df.columns if col != 'Year' ] ] # moving column to first position of a df
```
