import xlrd
import xlsxwriter

PRWB = xlrd.open_workbook('prsheet.xlsx')
PRSHEET= PRWB.sheet_by_index(0)
PRSHEET.cell_value(0, 0)
X = []

for i in range(PRSHEET.nrows):
    a = PRSHEET.cell_value(i, 2)
    X.append(a)
    parsed= map(str, X)[2:]

print (parsed)

IPAMWB = xlsxwriter.Workbook('pripam.xlsx')
IPAMSHEET= IPAMWB.add_worksheet('Sheet 1')

for t in parsed:
    IPAMSHEET.write(0, 0, t)

IPAMWB.close()

# row = 0
# col = 0
#
# for name, score in (parsed):
#     worksheet.write(row, col, name)
#     worksheet.write(row, col + 1, score)
#     row += 1
#

#IPAMSHEET.write(0, 0, 'parsed')
#cols = ["B"]
#for index, col in enumerate(cols):
#    value = parsed
#    IPAMSHEET.write(index, value)


#IPAMWB.save('pripam.xls')

#for row_index, row_contents in enumerate(parsed):

#    for column_index, cell_value in enumerate(row_contents):
#        IPAMSHEET.write(row_index, column_index)




#for i in range(PRSHEET.nrows):
#    a = str(PRSHEET.cell_value(i, 2))
    #print("\n".join(a.split("\n")[:]))
#    print ("\n".split(a))
