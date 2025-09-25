import pandas as pd
from sqlalchemy import create_engine
import urllib
import os

excel_file = 'excel_files/data.xlsx'
table_name = 'Average_PF'
server = os.getenv("DB_SERVER")
database = os.getenv("DB_DATABASE")

df = pd.read_excel(excel_file)
df.columns = df.columns.str.strip()
df = df[['Timestamp', 'Average_PF']]

# Use Windows Authentication (Trusted Connection)
params = urllib.parse.quote_plus(
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={server};DATABASE={database};Trusted_Connection=yes;"
)

engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")

df.to_sql(table_name, con=engine, if_exists='replace', index=False)
print(f"{len(df)} rows inserted successfully!")
