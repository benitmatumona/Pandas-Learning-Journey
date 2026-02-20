import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'], 
        'Score': [85, 92, 78, 59]}
df = pd.DataFrame(data)

#This is a function that returns the grades for each score
def add_grade(df):
    grade = []
    for score in df['Score']:
        if score >= 100:
            grade.append('A')
        elif 80 <= score < 90:
            grade.append('B')
        elif 70 <= score < 80:
            grade.append('C')
        else:
            grade.append('F')
    df['Grade'] = grade
    return df
print(add_grade(df))