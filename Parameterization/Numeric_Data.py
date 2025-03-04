import openpyxl


def main():
    file_path = "C:\\Users\\HP\\Desktop\\SDET\\Parameterization\\Demo.xlsx"

    wb = openpyxl.load_workbook(file_path)
    sheet = wb["Sheet3"]

    numeric_data = sheet.cell(row=2, column=2).value

    print(numeric_data)


if __name__ == "__main__":
    main()
