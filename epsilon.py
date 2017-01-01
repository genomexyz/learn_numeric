#!/usr/bin/python

import sys
import numpy

maks = 1.0
mins = 0.0

while True:
	test = (maks + mins) / 2.0
	if (1.0 + test) != 1.0:
		maks = test
	else:
		maks = test
		break
	if (1.0 + test) == 1.0:
		mins = test
print 'the epsilon is %.50f' % (maks)
