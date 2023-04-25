Group-Bys
```python
df_worker_count = df_ece_worker.groupby(['oin','year_date','job_title','hourly_pay_derived'], as_index=False)['user_id'].nunique()
```

```python
df_agg = df.groupby("continent").agg({"country": "count", "population": ["sum", "min", "max"]})
```
<img width="692" alt="image" src="https://user-images.githubusercontent.com/42124199/220915894-a6865aa6-79a1-4156-8b31-0b748fc54405.png">

```python
def q75(x):
        return x.quantile(0.75)

    df_job_dim = df_worker_fact_by_month.groupby(['job_title','job_title_updated'],as_index=False).agg({'hourly_pay_derived':['mean','median',q75,'max']}).round(2)
    
    #used to flatten table after group by
    # method 1
    df.columns = ['_'.join(col).rstrip('_') for col in df.columns.values]
    # method 2
    df = df.droplevel(axis=1, level=1).reset_index()
```
useful links: 
1. https://pbpython.com/groupby-agg.html
