import openpyxl


def main():
    file_path = "C:\\Users\\HP\\Desktop\\SDET\\Parameterization\\Demo.xlsx"

    wb = openpyxl.load_workbook(file_path)
    sheet = wb["Sheet1"]

    string_data = sheet.cell(row=1, column=1).value
    print(string_data)


if __name__ == "__main__":
    main()
