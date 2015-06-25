#!/usr/local/bin/python
#import csv

lines=open('Senarai_Order.txt').readlines()[8:-1]

total=0

for row in lines:
   rsplit=row.split(',')
   total=total+int(rsplit[2])

print 'Total:',total

open('orders.csv', 'w').writelines(lines)
