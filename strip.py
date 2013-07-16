import sys

def strip(inputFile):
	fileIn = open(inputFile,'rU')

	for line in fileIn:
		if line.find("IDENTIFIER") != -1:
			print line.replace("IDENTIFIER","").strip()

		elif line.find("STRING_LITERAL") != -1:
			print line.replace("STRING_LITERAL", "").strip()	

		elif line.find("OPERATOR") != -1:
			print line.replace("OPERATOR", "").strip()

		elif line.find("DELIMITER") != -1:
			print line.replace("DELIMITER", "").strip()

		elif line.find("IDENT") != -1:
			print line.replace("IDENT", "").strip() + "\t"	

		elif line.find("FLOATING_POINT") != -1:
			print line.replace("FLOATING_POINT", "").strip()	

		elif line.find("NUMBER") != -1:
			print line.replace("NUMBER", "").strip()	

		elif line.find("KEYWORD") != -1:
			print line.replace("KEYWORD", "").strip()	

		else:
			print line.strip()	

def main():	
	if len(sys.argv) != 2:
		print 'usage: python strip.py fileToStrip ', sys.argv
		sys.exit(1)
		
		inputFile = sys.argv[1]
		strip(inputFile)


if __name__ == '__main__':
		main()