#!/usr/bin/python

import sys
import numpy

N = 100000
maks = 1.0
mins = 0.0

for i in range (1,N):
	dostop = maks
	test = (maks + mins) / 2.0
	if (1.0 + test) != 1.0:
		maks = test
	if (1.0 + test) == 1.0:
		mins = test
print 'the epsilon is %.60f' % (maks)

#finding error machine
