def beautifulDays(i, j, k):
  return sum(abs(d-int(str(d)[::-1]))%k==0 for d in range(i,j+1))
print(beautifulDays(20,23,6))