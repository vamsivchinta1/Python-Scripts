### Engine Config
- an Engine references both a Dialect and a Pool, which together interpret the DBAPI’s module functions as well as the behavior of the database

![image](https://user-images.githubusercontent.com/42124199/191283663-9d3bcbd2-ea92-4e20-99d3-c49d31a9064f.png)

- The create_engine() function produces an Engine object based on a URL. 

Method 1
``` python

```

Method 2 - couldn't get it to work cause my server instance uses window's authenticate to sign into it
```python
from sqlalchemy.engine import URL
connection_url = URL.create(
    "mssql+pyodbc",
    username=r"DESKTOP-F1LO0GJ\vamsi",
    password="password",
    host="DESKTOP-F1LO0GJ",
    port=53017,
    database="Active_Graf_DWH",
    trusted_connection= 'yes',
    query={
        "driver": "ODBC Driver 17 for SQL Server",
        #"authentication": "ActiveDirectoryIntegrated",
    },
)

engine = db.create_engine(connection_url)

df = pd.read_sql("SELECT @@SERVERNAME AS 'Server Name'", engine)
df.head()
```
