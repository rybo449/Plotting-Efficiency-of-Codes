def searchGreaterNotSorted(L, v):
	count = 0
	for i in L:
		if i>=v:
			count+=1
	return count


# Performs search in sorted L (ascending order).
# L is sorted.
def searchGreaterSorted(L, v):
	j = len(L)
	for i in xrange(j):
		if L[i] >= v:
			break	
	return j - i


# Performs binary search in sorted L (ascending order).
def searchGreaterBinSearch(L, v):
	high = len(L) - 1
	low = 0
	size = len(L)
	while low < high:
		mid = (low + high)//2
		midvalue = L[mid]
		if v > midvalue:
			low = mid + 1
		elif v < midvalue:
			high = mid - 1
		elif v == midvalue:
			while v == L[mid] and mid<len(L) - 1:
				mid += 1
			return size - mid
		
	return size - low


# Performs range search in sorted L (ascending order).
def searchInRange(L, v1, v2):
	low = searchGreaterBinSearch(L, v1)
	high = searchGreaterBinSearch(L, v2)
	return high - low


