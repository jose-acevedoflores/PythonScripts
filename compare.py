import sys

def compareFunction(inputFile, fileToCompare):
	dicFirst = {}										 
	dicSecond = {}
	index = 0
	elements = 0
	count = 0
	firstText = open(inputFile, 'rU')
	secondText = open(fileToCompare, 'rU')
	for line in firstText:
		dicFirst[index] = line.strip()		 # fills the dictionary with the index as the key and the line as the value 
		index += 1
	index = 0			 # Reset the index for the second text
	for line in secondText:
		dicSecond[index] = line.strip()		# fills the dictionary with the index as the key and the line as the value
		index += 1
	
	iterator = dicSecond.iteritems()
	for tempTuple in dicFirst.items():					# Goes through all the tuples in dicFirst, they consist of index and string
		compare = iterator.next() # compare is equal to the tuple in dicSecond that has index element and element increases when the tuple changes	 
		if tuple[1] != compare[1]:																																							# i.e if tuple is the first one element is 0 
			print tempTuple[1],': is NOT equal to: ', compare[1] , "line ", elements+1
			count += 1								 # if they are not equal count goes up so ---
			
		elements += 1
		
	if count == 0:								 # --- if count equals 0 at the end there wasn't a line that was not equal
		print 'They are the same'

	
	firstText.close()
	secondText.close()

def main():
	if len(sys.argv) != 3:
		print 'usage: python compare.py file.txt filetocompare.txt', sys.argv
		sys.exit(1)
	
	inputFile = sys.argv[1]
	fileToCompare = sys.argv[2]
	compareFunction(inputFile, fileToCompare)

	
	

if __name__ == '__main__':
	main()