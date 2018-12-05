import sys
import string
def main():
	
	filename = sys.argv[1]
	
	f = open(filename, "r")
	
	unit = f.read(1)
	first = ''
	second = ''
	remaining_units = []
	while (unit != ''):
		if(unit == '\n'):
			unit = f.read(1)
			continue
	
		if(first == ''):
			#init 
			first = unit
			unit = f.read(1)
			continue
		#normal loop
		second = unit
		if ((first.isupper() and second.islower()) or (first.islower() and second.isupper())):
			if (first.upper() == second.upper()):
				#obliterate
				if (remaining_units == []):
					first = f.read(1)
				else:
					first = remaining_units[-1]
					del remaining_units[-1]
			else:
				remaining_units.append(first)
				first = second
		else:
			remaining_units.append(first)
			first = second
			
		unit = f.read(1)
		
		if(unit == ''):
			#store the last one back in to the list 
			remaining_units.append(first)
					
	print len(remaining_units)

	
	
if __name__ == "__main__":
	main()