#!/usr/bin/python

import sys
import numpy

maks = 1.0
mins = 0.0
frag = 0

while True:
	frag = frag + 1
	test = (maks + mins) / 2.0
	if (1.0 + test) != 1.0:
		maks = test
	else:
		maks = test
		break
print 'the epsilon is %.50f' % (maks)
print 'penjumlahan 1 + epsilon = %.50f' % (1+maks)
print 'bentuk pecahan dari epsilon adalah 1/2^%i' % (frag)
