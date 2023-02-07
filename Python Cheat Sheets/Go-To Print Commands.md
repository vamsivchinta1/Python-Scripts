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

```python
print(  'df_wpap_worker_fact_by_month:'
        ,'\n\t', os.path.split(fp)[-1]
        ,'\n\t',df_wpap_worker_fact_by_month.shape,'\n\t',df_wpap_worker_fact_by_month.columns.values.tolist()
        ,'\n\t','# of User ID, Job Title, OINs:', df_wpap_worker_fact_by_month[['user_id','job_title','oin']].drop_duplicates().reset_index(drop=True).shape[0]
        ,'\n\t','# of User ID, Job Titles:', df_wpap_worker_fact_by_month[['user_id','job_title']].drop_duplicates().reset_index(drop=True).shape[0]
        ,'\n\t','# of User IDs:',df_wpap_worker_fact_by_month['user_id'].drop_duplicates().reset_index(drop=True).shape[0]
        ,'\n\t','timeframe:',df_wpap_worker_fact_by_month['date'].min(),'-',df_wpap_worker_fact_by_month['date'].max()
        ,'\n\t','# of Months:', df_wpap_worker_fact_by_month['date'].drop_duplicates().reset_index(drop=True).shape[0]
        ,'\n\t','# of Programs:', df_wpap_worker_fact_by_month['oin'].drop_duplicates().reset_index(drop=True).shape[0]
)
```
