#!/usr/bin/python

#created by @genomexyz

import numpy as np
import random

#setting
iterasi = 1000
pool = 100
ubound = 10.
dbound = -10.
survive = 30
mutate = 0.2
target = 0
errtarget = 0.00000001


#search for the lowest val
def fitness(x, y):
#booth function
#global minimum f(1,3) = 0, search area -10 10
	return (x + 2*y + -7)**2.0 + (2*x + y - 5)**2.0

def breeding(xy1, xy2):
	b1 = random.uniform(0,1)
	return (1.0-b1) * xy1 + b1 * xy2

def mutation(xy):
	return xy*random.uniform(0.9,1)

print fitness(10,10)
print breeding(10,7)
#print random.randrange(0,10)
#print random.uniform(0,1)

#################
#init population#
#################

population = []

for i in xrange(pool):
	population.append([random.uniform(dbound, ubound), random.uniform(dbound, ubound)])

population = np.asarray(population)

#real action
for iterator in xrange(iterasi):

###############
#check fitness#
###############
	populationfit = np.zeros((pool))
	for i in xrange(pool):
		populationfit[i] = fitness(population[i,0], population[i,1])
	rankfit = np.argsort(populationfit)

#check fitness, is this the solution we want?
	print 'solution in in iteration ', iterator
	print population[rankfit[0]]
	print 'fitness', rankfit[0]
	if abs(rankfit[0]-target) < errtarget:
		break

#sorting population
	populatioNew = np.zeros((pool, 2))
	for i in xrange(pool):
		populatioNew[i] = population[rankfit[i]]
	populationfit.sort()



###########
#selection#
###########

	populatioNew = populatioNew[:survive]
	populationfit = populationfit[:survive]

###########
#crossover#
###########

	poolmating = np.zeros((pool-survive, 2))
	rolet = np.zeros((survive+1))
	rolet[0] = 0
#define domain of probability


	totprob = 0
	for i in xrange(survive):
		totprob += i+1
	for i in xrange(survive):
		rolet[i+1] = rolet[i] + survive - i

	#print rolet

#define mating partner
	for i in xrange(pool-survive):
#toss the ball for the rolet!
		balland = random.uniform(0, totprob)
		for j in xrange(survive):
			if balland < rolet[j+1]:
				choosenidx = j
				break
		poolmating[i] = populatioNew[choosenidx]
	#print poolmating


	newgen = np.zeros((pool-survive, 2))
	for i in xrange((pool-survive)/2):
		x1 = breeding(poolmating[i,0],poolmating[i+1,0])
		x2 = breeding(poolmating[i+1,0],poolmating[i,0])
		y1 = breeding(poolmating[i,1],poolmating[i+1,1])
		y2 = breeding(poolmating[i+1,1],poolmating[i,1])
		#print i*2, i*2+1
		newgen[i*2] = x1,y1
		newgen[i*2+1] = x2,y2
	#print newgen

##########
#mutation#
##########

	for i in xrange(len(newgen)):
		chancemutation = random.uniform(0,1)
		if chancemutation < mutate:
			if random.uniform(0,1) < 0.5:
				newgen[i,0] = mutation(newgen[i,0])
			else:
				newgen[i,1] = mutation(newgen[i,1])

##########
#assemble#
##########

	population[:survive] = populatioNew[:]
	population[survive:] = newgen[:]
