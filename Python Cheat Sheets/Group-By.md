Group-Bys
```python
df_worker_count = df_ece_worker.groupby(['oin','year_date','job_title','hourly_pay_derived'], as_index=False)['user_id'].nunique()
```
