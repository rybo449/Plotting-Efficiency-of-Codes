# Functions for students to implement.
naive = []
def buildNaive(points,n):
	del naive[:] #erasing previous data
	for i in points:
   		naive.append(i)
	#your code here
	return None


onedim = []
def buildOneDim(points,n):
	del onedim[:] #erasing previous data
	for i in xrange(n):
		onedim.append([])

	dim = 1/float(n)
	for i in points:
		onedim[int(i[0]//dim)].append(i)
	#your code here

	return None

twodim = []
def buildTwoDim(points,n):
	del twodim[:] #erasing previous data
	for i in xrange(n):		
		twodim.append([])
		for j in xrange(n):
			twodim[i].append([])
	dim = 1/ float(n)
	for i in points:
		twodim[int(i[0]//dim)][int(i[1]//dim)].append(i)
	#your code here

	return None

def queryNaive(x0, y0, x1, y1):
	count = 0
	for i in naive:
		if i[0] >= x0 and i[0] <= x1 and i[1] >= y0 and i[1] <= y1:
			count += 1
	#your code here
	#print count
	return count

def queryOneDim(x0, y0, x1, y1):
	count = 0
	length = len(onedim)
	dim = 1/float(length)
	l = int(x0//dim)
	r = int(x1//dim)
	for i in onedim[l]:
		if x0 <= i[0] and x1 >= i[0] and y0 <= i[1] and y1 >= i[1]:
			count += 1
	for i in onedim[r]:
		if x0 <= i[0] and x1 >= i[0] and y0 <= i[1] and y1 >= i[1]:
			count += 1
	for i in xrange(l+1,r):
		for j in onedim[i]:
			if y0 <= j[1] and y1 >= j[1]:
				count += 1  
	#your code here

	return count

def queryTwoDim(x0, y0, x1, y1):
	count = 0
	length = len(twodim)
	dim = 1/float(length)
	left = int(x0//dim)
	right = int(x1//dim)
	bottom = int(y0//dim)
	top = int(y1//dim)
	for i in xrange(left + 1, right):
		for j in xrange(bottom + 1, top):
			count += len(twodim[i][j])
		for j in twodim[i][bottom]:
			if j[1] >= y0 and j[1] <= y1:
				count += 1
		for j in twodim[i][top]:
			if j[1] >= y0 and j[1] <= y1:
				count += 1

	for i in xrange(bottom, top + 1):
		for j in twodim[left][i]:
			if x0 <= j[0] and x1 >= j[0] and y0 <= j[1] and y1 >= j[1]:
				count += 1	
		for j in twodim[right][i]:
			if x0 <= j[0] and x1 >= j[0] and y0 <= j[1] and y1 >= j[1]:
				count += 1
	#your code here

	return count
