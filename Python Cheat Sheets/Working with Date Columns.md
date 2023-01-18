# Working w/ Dates
```python
df2['Date'] = pd.to_datetime(df.Year, format='%Y') #convert year column to date
df['datetime'] = pd.to_datetime(df['datetime']).dt.date
df['year'] = pd.DatetimeIndex(df['birth_date']).year #extracting year from date col
```
