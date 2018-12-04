#import string
import sys
import re 
from itertools import ifilter
from itertools import product
import sets

@profile
def main():
	
	filename = sys.argv[1]
	
	f = open(filename, "r")
	
	line = f.readline()
	
	IDs = []
	start = []
	dims = []
	
	overlap = 0
	
	usedCanvas = set()
	sharedCanvas = set()
	allCanvases = []
	doesntOverlap = 0
		
	while (line != ''):
		a = re.findall("[0-9]*",line)
		b = map(int, list(ifilter(None,a)))
		IDs.append(b[0])
		start.append((b[1], b[2]))
		dims.append((b[3], b[4]))
		
		xStart = start[len(start)-1][0]
		xEnd = xStart + dims[len(dims)-1][0]
		
		yStart = start[len(start)-1][1]
		yEnd = yStart + dims[len(dims)-1][1]
		
		
		
		elfCanvas = set()
		if(not bool(usedCanvas)):
			usedCanvas = set(product(range(xStart, xEnd), range(yStart, yEnd)))
			## Empty set is always in all the sets
			allCanvases.append(usedCanvas)
		else:
			
			elfCanvas = set(product(range(xStart, xEnd), range(yStart, yEnd)))
			shared = set()
			shared = set.intersection(usedCanvas, elfCanvas)
			
			if( bool(shared)):
				overlap += len(shared)
				sharedCanvas.update(shared)
			
				
			usedCanvas.update(elfCanvas)
			allCanvases.append(elfCanvas)
		
		line = f.readline()
		
		
	print "Shared canvas: ", len(sharedCanvas)
	
	id = 1
	for canvas in allCanvases:
		if(not bool(set.intersection(sharedCanvas,canvas))):
			print "Canvas n:" , id
		id += 1
	
if __name__ == "__main__":
	main()