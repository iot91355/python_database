import pandas as pd

excel_file = 'excel_files/data.xlsx'
df = pd.read_excel(excel_file)

print(df.columns)  # This will show the exact column names
