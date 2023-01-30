### Joining
```python
df = pd.merge(df1, df2, on='A', how='inner')
```
```python
df = pd.concat([df1, df2])
```
```python
#perform outer join
outer = df1.merge(df2, how='outer', indicator=True)

#perform anti-join
anti_join = outer[(outer._merge=='left_only')].drop('_merge', axis=1)

#view results
print(anti_join)

  team  points
3    D      14
4    E      30
```
