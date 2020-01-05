#!/usr/bin/python3

import operator
import sys
import numpy as np
import os

def createDataSet(directory):
	g = []
	l = []
	fnames = []
	g2 = []

	fl = os.listdir(directory)	

	for filename in fl:
		fnames.append(filename)
	
	for answer in fnames:
		l.append(float(answer.split("_")[0]))

	
	for textfile in fnames:
		f = open(directory + "/" + textfile, "rt")
		tGroup = f.read()
		tGroup = tGroup.replace('\n', '')
		g1 = list(tGroup)
		for i in g1:
			if i == '\n':
				g1.remove('\n')
		g = [float(x) for x in g1]
		
				#if n is '\n':
				#	continue
				#tGroup.append(float(n))
		
		g2.append(g)
		#group2 = np.array(g2)
		f.close()
		
	
	#print(labels)
	#print(group)
	#print(type(group2))
	group2 = np.array(g2)
	return group2, l


def classify0(inX, dataSet, labels, k):

	dataSetSize = dataSet.shape[0]
	diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
	sqDiffMat = diffMat ** 2
	sqDistances = sqDiffMat.sum(axis = 1)
	distances = sqDistances ** 0.5
	s = distances.argsort()
	classCount = {}
	for i in range(k):
		voteIlabel = labels[s[i]]
		classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1

	scc = sorted(classCount.items(), key = operator.itemgetter(1), reverse = True)
	return scc[0][0]


def getError(k):
	
	knnanswer, answer = getAnswer(k)
	count = 0
	#print(knnanswer)
	#print(answer)
	for i in range(len(answer)):
		if knnanswer[i] != answer[i]:
			count = count + 1
	

	return int(count/len(answer) * 100)
	



def printError():
	for i in range(1, 20):
		#print(i)
		if i % 2 != 0:
			print(getError(i))


def getAnswer(k):
	
	knnanswer = []
	for inX in inXgroup:
		knnanswer.append(classify0(inX, group, labels, k))


	return knnanswer, answer

		

group, labels = createDataSet(sys.argv[1])
inXgroup, answer = createDataSet(sys.argv[2])	
printError()



	
                             
				
