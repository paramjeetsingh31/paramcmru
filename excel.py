import xlrd

wb = xlrd.open_workbook('data/example.xlsx')
sh1 = wb.sheet_by_name(u'Sheet1')

print sh1.col_values(0)  # column 0
print sh1.col_values(1)  # column 1

sh2 = wb.sheet_by_name(u'Sheet2')

x = sh2.col_values(0)  # column 0
y = sh2.col_values(1)  # column 1

import matplotlib.pyplot as plt
plt.plot(x, y)
plt.savefig('/home/ec2017b212/roshanlal/graphline/excel.py')