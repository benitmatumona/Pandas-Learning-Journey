import pandas as pd

data = {'Date': ['2020-01-01', '2020-01-02', '2020-01-03', '2020-01-04', '2020-01-05'],
        'Stock Price': [500, 520, 550, 580, 600]}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
df['Daily Returns'] = df['Stock Price'].pct_change()
df['Cumulative Returns'] = (1 + df['Daily Returns']).cumprod()
print(df)