from xlwt import *

book = Workbook()
sheet = book.add_sheet('Sheet1')
sheet.write(0, 0, label = 'Row 0, Column 0 Value')
book.save('myExcel.xls')
