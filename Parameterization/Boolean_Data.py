import openpyxl


def main():
    file_path = "C:\\Users\\HP\\Desktop\\SDET\\Parameterization\\Demo.xlsx"

    wb = openpyxl.load_workbook(file_path)
    sheet = wb["Sheet4"]

    boolean_data = sheet.cell(row=4, column=1).value

    print(boolean_data)


if __name__ == "__main__":
    main()
