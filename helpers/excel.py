import xlsxwriter


def formatWorkSheet(workbook, sheetName):
    worksheet = workbook.add_worksheet(sheetName)
    bold = workbook.add_format({'bold': True})
    worksheet.write('A1', 'Words', bold)
    worksheet.write('B1', 'Meanings', bold)
    worksheet.write('C1', 'Example', bold)
    return worksheet
