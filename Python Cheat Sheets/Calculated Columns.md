Calculated columns in pandas    
logic done in sql
```sql
# 
SELECT 
  *, 
  tip/size AS tip_per_person 
FROM 
  tips;
```
same logic done in python 
```python
# 
df_tips.assign(tips_per_person = df_tips['tip']/df_tips['nbr_of_ppl_in_party'])
```
```python
#add 'class' column using case-statement logic
df['class'] = np.where(df['points']<9, 'Bad',
              np.where(df['points']<12, 'OK',
              np.where(df['points']<15, 'Good', 'Great')))

#view updated DataFrame
df

	player	points	class
0	1	6	Bad
1	2	8	Bad
2	3	9	OK
3	4	9	OK
4	5	12	Good
5	6	14	Good
6	7	15	Great
7	8	17	Great
8	9	19	Great
9	10	22	Great
```
