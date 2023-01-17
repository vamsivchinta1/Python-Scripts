# checking data types
```python
print(df.dtypes)
type(a) # id type of object
```
```python
df = df.apply(pd.to_numeric) # convert dtype of all columns of DataFrame
df[["a", "b"]] = df[["a", "b"]].apply(pd.to_numeric) # convert dtype of just columns "a" and "b"
df['column name'] = df['column name'].astype(np.int64)
```
