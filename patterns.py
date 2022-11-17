n=5
'''   
    *
   ***   
  *****  
 ******* 
*********
'''
# for i in range(n):
# 		print(" "*(n-i-1)+"*"*(2*i+1))
"""
	1 
	1 2
	1 2 3
	1 2 3 4
	1 2 3 4 5
"""
# for i in range(n):
# 	for j in range(i+1):
# 		print(j+1,end=" ")
# 	print()
"""
1 
2 1
3 2 1
4 3 2 1
5 4 3 2 1
"""
# for i in range(n):
# 	for j in range(i,-1,-1):
# 		print(j+1,end=" ")
# 	print()
"""
1 
2 2
3 3 3
4 4 4 4
5 5 5 5 5
"""
# for i in range(n):
# 	for j in range(i,-1,-1):
# 		print(i+1,end=" ")
# 	print()

"""
5 
4 4
3 3 3
2 2 2 2
1 1 1 1 1
"""
# for i in range(n):
# 	for j in range(i,-1,-1):
# 		print(n-i,end=" ")
# 	print()


"""
5 
5 4
5 4 3
5 4 3 2
5 4 3 2 1
"""
# for i in range(n):
# 	for j in range(i+1):
# 		print(n-j,end=" ")
# 	print()

"""
5 
4 5 
3 4 5 
2 3 4 5 
1 2 3 4 5 
"""
# for i in range(n):
# 	for j in range(i,-1,-1):
# 		print(n-j,end=" ")
# 	print()

"""
        1
      2 1
    3 2 1
  4 3 2 1
5 4 3 2 1
"""
for i in range(n):
	for k in range(n-i-1):
		print(" ",end=" ")
	for j in range(i,-1,-1):
		print(j+1,end=" ")
	print()

	