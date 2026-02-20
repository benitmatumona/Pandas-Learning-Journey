import pandas as pd

data = {'Date':['2022-01-01', '2022-01-15', 
        '2022-02-01','2022-02-15','2022-03-01'],
        'Sales':[100, 200, 150, 250, 300]}
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

#This is a function that returns the sum of the sales for each month
def total_sales(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby(df['Date'].dt.to_period('M'))['Sales'].sum().reset_index()

print(total_sales(df))
