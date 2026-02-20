import pandas as pd

data = {'Name': ['John', 'Alice', 'Bob', 'Marry', 'Data'],
        'Salary': [50000, 60000, 55000, 70000, 70000]}
df = pd.DataFrame(data)

#Creates a function that finds the employee with the highest salary
def highest_salary(df: pd.DataFrame)-> pd.DataFrame:
    return df[df['Salary'] == df['Salary'].max()]

print(highest_salary(df))