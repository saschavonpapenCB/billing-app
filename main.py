import pandas as pd

def get_csv(file):
    return pd.read_csv(file)

def get_excel(file):
    return pd.read_excel(file)

csv_data = get_csv('example_data.csv')
print("CSV data: \n")
print(csv_data)

excel_data = get_excel('example_data.xlsx')
print("Excel data: \n")
print(excel_data)
