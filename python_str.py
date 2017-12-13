import csv
from io import StringIO


str_obj = StringIO()
writer = csv.writer(str_obj,
                    delimiter=',',
                    quotechar='|',
                    quoting=csv.QUOTE_MINIMAL,
                    lineterminator='\n')

x = [['lala', 'popo'], ['hehe', 'hoho']]

for elem in x:
        writer.writerow(elem)

bytes_obj = bytes(str_obj.getvalue().encode('utf8'))

