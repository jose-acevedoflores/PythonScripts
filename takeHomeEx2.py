import sys

def fileAnalysis(inputFile):

	filePath = open(inputFile, 'rU')


	filePath.close()


def AllImter(listA, listB):
	
	print "none"

def ParallelInter(listA, listB):
	index = 0;
	newList = []
	for element in listA:

		newList.append(element)
		if index < len(listB):
			newList.append(listB[index])
		index = index +1

	while index < len(listB):
		newList.append(listB[index])
		index = index+1	

	print newList


def main():
	if len(sys.argv) != 1:
		print 'usage: python compare.py', sys.argv
		sys.exit(1)
	
	a = [1,2]
	b = [3,4] 
	ParallelInter(a,b) 


	
	

if __name__ == '__main__':
	main()