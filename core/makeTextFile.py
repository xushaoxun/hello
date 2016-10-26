#!/usr/bin/python

'''make Text file'''

import os

ls = os.linesep

while True:
    fname = raw_input('file name:')
    if os.path.exists(fname):
        print fname, ' exists'
    else:
        print 'use ', fname
        break

lines  = []
while True:
    line = raw_input('line, end with .:')
    if line == '.':
        break
    lines.append(line + ls)

with open(fname, 'w') as f:
    f.writelines(lines)
print 'OK'


