def pageCount(grades):
	l=[]
	for i in grades:
		if i<38:
			l.append(i)
		elif i%5 >=3:
			l.append(5*((i+5)//5))
		else:
			l.append(i)
	return l
	
print(pageCount([73,67,38,33]))