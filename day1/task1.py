import sys 


def main():
	
	filename = sys.argv[1]
	
	f = open(filename, "r")
	
	line = f.readline()
	sum = 0
	
	while (line != ''):
		sum += int(line)
		line = f.readline()
		
	print sum
	

	
if __name__ == "__main__":
	main()
	
	