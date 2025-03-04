import openpyxl


def main():
    file_path = "C:\\Users\\HP\\Desktop\\SDET\\Parameterization\\Demo.xlsx"

    wb = openpyxl.load_workbook(file_path)
    sheet = wb["Sheet6"]

    num_string = sheet.cell(row=1, column=1).value

    print(num_string)


if __name__ == "__main__":
    main()
