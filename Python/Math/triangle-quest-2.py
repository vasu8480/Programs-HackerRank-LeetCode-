for i in range(1,int(input())+1):
        print(((10**i-1)//9)**2)
#-----------------------------------------------------------#
for i in range(1,int(input())+1):
	print(''.join(map(str,list(range(1,i)))), ''.join(map(str,list(range(i,0,-1)))), sep='')

for i in range(1,int(input())+1):     
    for j in range(1,i+1):
        print(j,end="")
    for k in range(i-1,0,-1):
        print(k,end="") 
    print()

