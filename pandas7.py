import pandas as pd

data = {'Product': ['Product A', 'Product B', 'Product C', 'Product D'],
        'Price': [10.99, 9.99, 12.99, 8.99]}
df = pd.DataFrame(data)

# this is a function that calculates the avarage price
def avarage(df: pd.DataFrame) -> float:
    return df['Price'].mean()
print(avarage(df))