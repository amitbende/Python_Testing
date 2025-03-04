import openpyxl


def main():
    file_path = "C:\\Users\\HP\\Desktop\\SDET\\Parameterization\\Demo.xlsx"

    wb = openpyxl.load_workbook(file_path)
    sheet = wb["Sheet4"]

    last_row_index = sheet.max_row - 1

    print(last_row_index)


if __name__ == "__main__":
    main()
