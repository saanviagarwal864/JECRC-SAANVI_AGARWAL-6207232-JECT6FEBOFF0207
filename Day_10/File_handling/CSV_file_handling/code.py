'''
CSV FILE HANDLING
'''
import csv
from datetime import date
file=open('expense.csv','a+', newline='') ##no spaces between lines
# w=csv.writer(file)
# w.writerow(['DATE','CATEGORY','AMOUNT']) ##column names
# w.writerows([
#     [date.today(),'Travel',2000],
#     [date.today(),'Food',3000],
#     [date.today(),'Entertainment',4000],
#     [date.today(),'Stay',8000]
# ])

r=csv.reader(file)

file.seek(0)

print(r) ##<_csv.reader object at 0x0000026D950DE380>
print(list(r)) ##[['DATE', 'CATEGORY', 'AMOUNT'], ['2026-03-10', 'Travel', '2000'] like this data will be printed


file.close()
