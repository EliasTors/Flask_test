import pandas as pd

data = pd.read_excel('bok1.xlsx')
data = data.replace(" cm", "", regex=True).replace(" m", "", regex=True).replace(" %", "", regex=True)

data.sort_values(by=['Country'], inplace=True)



data.to_csv('data.csv')

