import numpy as np


def base_points():
	i = 0
	text = []

	with open("score.txt", 'r', encoding="utf8") as file:
		#with open("base_points.txt", 'w') as file1:
		for line in file:
			line = line.split()
			i += 1
			text.append(line)

	text[0][0] = text[0][0][1:]#    without waste
	#print(i)
	#print(text)


	dict = {"Russia" : [0, 0, 0]}

	for trios in text[-68:]:#    10 first percent
		#print(trios)
		if trios[0] in dict.keys():
			dict[trios[0]][0] += int(trios[1][0])
			dict[trios[0]][1] += int(trios[1][2])
			dict[trios[0]][2] += 1
		else:
			dict.update({trios[0] : [int(trios[1][0]), int(trios[1][2]), 1]})
		if trios[2] in dict.keys():
			dict[trios[2]][0] += int(trios[1][2])
			dict[trios[2]][1] += int(trios[1][0])
			dict[trios[2]][2] += 1
		else:
			dict.update({trios[2] : [int(trios[1][2]), int(trios[1][0]), 1]})
		#print(dict)
		
	#print(dict)
	return dict, text

def make_base(dict, text):
	base = []
	for trios in text[:-69]:#    last 90 percent
		if trios[0] in dict.keys():
			base += [dict[trios[0]][0] / float(dict[trios[0]][2])] + [dict[trios[0]][1] / float(dict[trios[0]][2])]
			
			dict[trios[0]][0] += int(trios[1][0])
			dict[trios[0]][1] += int(trios[1][2])
			dict[trios[0]][2] += 1
		else:
			base += [0] + [0]
			dict.update({trios[0] : [int(trios[1][0]), int(trios[1][2]), 1]})
			
		if trios[2] in dict.keys():
			base += [dict[trios[2]][0] / float(dict[trios[2]][2])] + [dict[trios[2]][1] / float(dict[trios[2]][2])]

			dict[trios[2]][0] += int(trios[1][2])
			dict[trios[2]][1] += int(trios[1][0])
			dict[trios[2]][2] += 1
		else:
			base += [0] + [0]
			dict.update({trios[2] : [int(trios[1][2]), int(trios[1][0]), 1]})
	
		if int(trios[1][0]) > int(trios[1][2]):#    won first
			base += [1]
		if int(trios[1][0]) < int(trios[1][2]):#    won second
			base += [2]
		if int(trios[1][0]) == int(trios[1][2]):#    draw
			base += [3]
		
	base = np.array(base).reshape(len(base) / 5, 5)
	'''print(base)
	print(base.shape)'''
	with open("base.txt", 'w') as file:
		for i in range(len(base)):
			for j in range(len(base[i])):
				file.write(str(base[i][j]) + '\t')
			file.write('\n')

dict, text = base_points()
make_base(dict, text)
