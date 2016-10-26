#!/usr/bin/python
# coding:utf-8

import os

def readf(fname):
    try:
        with open(fname) as f:
            for line in f:
                print line.strip()
    except IOError as e:
        print e

def writef(fname):
    with open(fname, 'w') as f:
        while True:
            line = raw_input('content to write, ENTER to exists')
            if not line: break

            f.write(line + os.linesep)
    print 'Done. wirte to [%s]' % fname


if __name__ == '__main__':
    mode = raw_input('(r)ead or (w)rite?')

    funcs = {'r': readf, 'w': writef}

    if mode in funcs.keys():
        fname = raw_input('file name:')
        funcs[mode](fname)
    else:
        print 'use r|w'
