import sys
import shlex
import operator

def fileAnalysis(inputFile):

	filePath = open(inputFile, 'rU')
	words = {} # Dictionary to hold the words in the text file. Format: {(word:key, number of ocurrences, line it appears)} 
	wordsLines = {}
	lineNumber = 1

	for line in filePath:
		temp = shlex.split(line)
		for word in temp:
			word = word.lower()
			wordCount = words.get(word, "0")
			lineAppear = wordsLines.get(word, "")
			wordsLines[word] = lineAppear + str(lineNumber) + ","
			words[word] = int(wordCount)+1
		lineNumber = lineNumber+1

# Sort the list dictionary 
	newList = sorted(words.iteritems(), key=operator.itemgetter(1) , reverse=True)	

	for element in newList: 
		lineNumbers = wordsLines[element[0]]
		print "Word '" + element[0] + "' appears a total of "+ str(element[1]) + " times. It appears in lines " + lineNumbers


	filePath.close()


def main():
	if len(sys.argv) != 2:
		print 'usage: python compare.py filePath.txt', sys.argv
		sys.exit(1)
	
	filePath = sys.argv[1]
	fileAnalysis(filePath)

	
	

if __name__ == '__main__':
	main()