# -*-coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import time
import datetime
import codecs
import xlrd
#import xlwt

def readXls():
    w_file = open('14.xml', 'w')
    filename = '14.xls'
    book = xlrd.open_workbook(filename)
    sh = book.sheet_by_index(0)
    head = sh.row_values(0)
    
    print 'rows: ', sh.nrows
    w_file.write('<add>\n')
    for i in range(1, sh.nrows):
        w_file.write('<doc>\n')
        col = sh.row_values(i)

        for j in range(1, len(head)):
            cell = sh.cell(i,j)
            #print cell.ctype, cell
            cell_value = cell.value
            if cell_value != '':
                if cell.ctype == 2:
                    value = int(cell_value)
                elif cell.ctype == 3:
                    timetuple = xlrd.xldate_as_tuple(cell_value, book.datemode)
                    tDate = datetime.datetime(*timetuple)
                    value = tDate.strftime('%Y-%m-%dT%H:%M:%SZ')
                else:
                    value = str(cell_value)
                
                field = '<field name="%s">%s</field>\n' %(head[j].lower(), value)
                w_file.write(field)
                
        w_file.write('</doc>\n')
        
    w_file.write('</add>\n')
    w_file.close()

if __name__ == "__main__":
    #testXlrd()
    readXls()