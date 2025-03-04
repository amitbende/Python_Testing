import openpyxl


def main():
    file_path = "C:\\Users\\HP\\Desktop\\SDET\\Parameterization\\Demo.xlsx"

    wb = openpyxl.load_workbook(file_path)
    sheet = wb["Sheet5"]

    last_column_index = sheet.max_column - 1

    print(last_column_index)


if __name__ == "__main__":
    main()
