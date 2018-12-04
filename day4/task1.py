import sys
import re 
import datetime
from collections import OrderedDict


def main():
	
	filename = sys.argv[1]
	
	f = open(filename, "r")
	
	line = f.readline()
	
	records = OrderedDict()
		
	while (line != ''):
		dt = re.search('\d{4}-\d{2}-\d{2} \d{2}:\d{2}', line)
		text = re.search(r'].*',line)
		dt_key =  datetime.datetime.strptime(dt.group(), '%Y-%m-%d %H:%M')
		records[dt_key] = text.group()[2:]
		line = f.readline()
		
		
	sorted_records = sorted(records.items(),key=lambda t:t[0])
	
	
	
	guards ={}
	current_guard = 0
	start = 0
	stop = 0
	for k, v in sorted_records:
		#print k, v
		re_m = re.findall('#[0-9]*', v)
		#print re_m.group()	
		if( re_m != []):
			re_m = re_m[0]
			if(re_m not in guards.keys()):
				current_guard = re_m
				guards[current_guard] = dict((el,0) for el in range(0,60))
			else:
				current_guard = re_m
		else:
			re_m = v 
			if(re_m == 'falls asleep'):
				start = k.minute
			elif (re_m == 'wakes up'):
				stop = k.minute
				for i in range(start,stop):
					guards[current_guard][i] = guards[current_guard][i] + 1
	
	times = {}
	for guard in guards.keys():
		times[guard] = sum(guards[guard].values())
		
	maximum = max(times, key=times.get)
	print (maximum, times[maximum])
	max_min = max(guards[maximum], key=guards[maximum].get)
	
	print (max_min, guards[maximum][max_min])
	
	##part 2 
	times = {}
	for guard in guards.keys():
		max_minute = max(guards[guard], key=guards[guard].get) ##Which minute is the most asleep
		times[guard] = (max_minute, guards[guard][max_minute])
	#print times	
	max_guard = 0
	max_minute = 0
	for guard in times.keys():
		if ( times[guard][1] > max_minute):
			max_minute = times[guard][1]
			max_guard = guard
	
	print "Guard , (minute, xTimes) ", (max_guard, times[max_guard])
	
if __name__ == "__main__":
	main()