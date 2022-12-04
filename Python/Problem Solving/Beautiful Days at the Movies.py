def beautifulDays(i, j, k):
  c=0
  for d in range(i,j+1):
    q=int(str(d)[::-1])
    if abs(d-q)%k==0:
      c+=1
  return c
print(beautifulDays(20,23,6))
#---------------------------------------------------------------------------------------------------
def beautifulDays(i, j, k):
  return sum(abs(d-int(str(d)[::-1]))%k==0 for d in range(i,j+1))
print(beautifulDays(20,23,6))