import openpyxl


def main():
    file_path = "C:\\Users\\HP\\Desktop\\SDET\\Parameterization\\Demo.xlsx"

    wb = openpyxl.load_workbook(file_path)
    sheet = wb["Sheet4"]

    row_size = sheet.max_row
    print(row_size)


if __name__ == "__main__":
    main()
