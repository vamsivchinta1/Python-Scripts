# Writing Data
```python 
df.to_excel('cat_kst_df.xlsx', sheet_name='Sheet_name_1')
```

```python 
# write to master workbook
with pd.ExcelWriter(os.path.join(cwd + '/3. Consumption Layer/JFS Data Mart/Cost_of_Turnover_Analysis.xlsx'), mode='w') as writer: 
     df_user_dim.to_excel(writer, sheet_name="dim worker", index=False)
     df_job_dim.to_excel(writer, sheet_name="dim job type", index=False)
```
