#! /usr/bin/python

import sys;

def szam(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False
def bemenet(s):
	try: return(open(s, 'r'))
	except: print("Nincs ilyen file!")


if len(sys.argv) > 1 : 
	f = bemenet(sys.argv[1])
	if f != None :
		f2 = open("eredmeny.txt", 'w')
		f2.write(f.readline().strip())
		x = 0
		for line in f :
			if(szam(line)):
				x = x + int(line)
			else : 	
				f2.write(' ' + str(x) + '\n' + line.strip())
				x = 0
		if x!=0 : f2.write(' ' + str(x))
		f.close()
		f2.close()
else : 
	print("Nincs argumentum!")
	
