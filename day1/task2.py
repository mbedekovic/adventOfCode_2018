import sys 
#from sets import set

def main():
	
	filename = sys.argv[1]
	
	f = open(filename, "r")
	
	line = f.readline()
	sum = 0
	
	list = []
	
	while (line != ''):
		list.append(int(line))
		line = f.readline()
	
	size = len(list)
	
	freq = set()
	
	flag = True
	i = 0
	while(flag):
		sum += list[i%size]
		i += 1
		
		if (sum in freq):
			flag = False
		else:
			freq.add(sum)
	
	print sum
	
if __name__ == "__main__":
	main()
	
	