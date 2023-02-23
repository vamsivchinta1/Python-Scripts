Group-Bys
```python
df_worker_count = df_ece_worker.groupby(['oin','year_date','job_title','hourly_pay_derived'], as_index=False)['user_id'].nunique()
```

```python
df_agg = df.groupby("continent").agg({"country": "count", "population": ["sum", "min", "max"]})
```
<img width="692" alt="image" src="https://user-images.githubusercontent.com/42124199/220915894-a6865aa6-79a1-4156-8b31-0b748fc54405.png">
