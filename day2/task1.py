import sys 
import re
import string
#from sets import set

def main():
	
	filename = sys.argv[1]
	
	f = open(filename, "r")
	
	line = f.readline()
	sum2 = 0
	sum3 = 0
	
	alpha = list(string.ascii_lowercase)
	
	while (line != ''):
		ex2 = 0
		ex3 = 0
		
		for letter in alpha:
			n = re.findall(letter,line)
			if len(n) == 2:
				ex2 += 1
			if len(n) == 3:
				ex3 += 1
		if (ex2 >= 1): 
			sum2 +=1
		if (ex3 >= 1):
			sum3 += 1
		
		
		line = f.readline()
	
	
	checksum = sum2*sum3
	
	print sum2
	print sum3
	print checksum
	
if __name__ == "__main__":
	main()
	
	