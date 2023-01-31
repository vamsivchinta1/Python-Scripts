```python
display(df1.head())
```

```python
print('\nRun ECE Worker Fact & Dim Pipeline \n--- read in data ----')
print(  'df_raw:','\n\t',df_raw.shape,'\n\t',df_raw.columns.values.tolist()
        ,'\n\t','# of User IDs:',df_raw['user_id'].drop_duplicates().reset_index(drop=True).shape[0]
        ,'\n\t # of Months:', df_raw['date'].drop_duplicates().reset_index(drop=True).shape[0]
        ,'\n\t # of Programs:', df_raw['oin'].drop_duplicates().reset_index(drop=True).shape[0]
)
```
<img width="273" alt="image" src="https://user-images.githubusercontent.com/42124199/215791057-baf1741f-9d24-4369-96bc-6e5eb08314cf.png">
