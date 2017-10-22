import os
from os import listdir
from os.path import isfile, join
import re

p = 'E:/Documents and Settings/Tiago/Desktop/EJHack/sentencas'

files = [f for f in listdir(p) if isfile(join(p, f))]

for f in files:

	with open(p+'/'+f, 'r') as myfile:
			lines = myfile.readlines()

	lines.reverse()
	line_id = 0
	last = -1
	same_line = 0
	for idy, line in enumerate(lines):
		split = line.split(' ')
		tamanho = len(split)
		b = 0
		for idx, elem in enumerate(split):
			match = re.match("-?Ju[i\u00ED]z", elem)
			if match:
				print(f)
				empty = 0
				for i in range(idx,tamanho):
					if(split[i] == ''):
						empty = empty + 1
						if(empty > 2):
							break
					elif(split[i][0] == ':'):
						same_line = 1
						break
					else:
						last = i
						if(split[i][-1] == ':'):
							print(split[i].encode('utf-8'))
							same_line = 1
							break
						print(split[i].encode('utf-8'))
				b = 1
				break
		line_id = idy
		if b == 1:
			break

	print()

	pr = 0

	if(same_line == 1):
		#print('Same Line IF')
		line = lines[line_id].split(' ')
		empty = 0
		for i in range(last+1,len(line)):
			if(line[i] == ''):
				empty = empty + 1
				if(empty > 2):
					break
			else:
				pr = 1
				print(line[i].encode('utf-8'))


	if(line_id < len(lines)-1 and pr == 0):
		#print('Line +1 IF')
		line = lines[line_id+1].lstrip(' ').rstrip('\n').split(' ')
		empty = 0
		for i in range(0,len(line)):
			if(line[i] == ''):
				empty = empty + 1
				if(empty > 2):
					break
			else:
				pr = 1
				print(line[i].encode('utf-8'))
	if(line_id < len(lines)-2 and pr == 0):
		#print('Line +2 IF')
		line = lines[line_id+2].lstrip(' ').rstrip('\n').split(' ')
		empty = 0
		for i in range(0,len(line)):
			if(line[i] == ''):
				empty = empty + 1
				if(empty > 2):
					break
			else:
				pr = 1
				print(line[i].encode('utf-8'))
	print()
