from xlwt import *

a = ['vvvfff', 'rrrrr', '']

book = Workbook()
sheet = book.add_sheet('Sheet1')

for index in range(len(a)):
    sheet.write(index, 0, a[index])
book.save('myExcel.xls')
