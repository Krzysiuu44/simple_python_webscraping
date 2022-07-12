import pandas as pd

read_file = pd.read_csv(r'plik.csv')
read_file.to_excel(r'nowy.xlsx', index = None, header=True)