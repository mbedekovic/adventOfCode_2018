import sys 
import re
import string
import Levenshtein
#from sets import set

def main():
	
	filename = sys.argv[1]
	
	f = open(filename, "r")
	
	line = f.readline()
	sum2 = 0
	sum3 = 0
	
	input = []
	similar = []
	while (line != ''):
		input.append(line)
		line = f.readline()
		
	for code in input:
		for str in input:
			if ((code != str) and not (code in similar)):
				if(Levenshtein.distance(code,str) == 1):
					similar.append(code)
					similar.append(str)
					
	print similar
				
				
if __name__ == "__main__":
	main()
	
	