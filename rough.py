def beautifulTriplets(d, arr):
		c = 0
		for i in range(len(arr)):
			for j in range(i+1,len(arr)):
				if arr[j] - arr[i] == d:
					for k in range(j+1,len(arr)):
						if arr[k] - arr[j] == d:
							c += 1
							break
		return c
print(beautifulTriplets(3,[1, 2, 4, 5, 7, 8, 10]))



