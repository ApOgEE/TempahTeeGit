#!/usr/local/bin/python

lines = open('Senarai_Order.txt').readlines()
open('Senarai.csv', 'w').writelines(lines[8:-1])
