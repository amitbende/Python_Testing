import openpyxl

file_path = "C:\\Users\\HP\\Desktop\\SDET\\Parameterization\\Demo.xlsx"

wb = openpyxl.load_workbook(file_path)
sheet = wb["Sheet2"]

string_data = sheet.cell(row=2, column=1).value
print(string_data)

