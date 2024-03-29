# File: Angry Professor.py
def designerPdfViewer(k,a):
		l=[i for i in a if i<=0]
		return "NO" if len(l)>=k else "YES"
print(designerPdfViewer(3 ,[-1, -3, 4, 2]))
#----------------------------------------------------------------------------------------------------
def designerPdfViewer(k,a):
		return "NO" if len([i for i in a if i<=0])>=k else "YES"

print(designerPdfViewer(3 ,[-1, -3, 4, 2]))
		
# File: Apple and Orange.py
def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    print(len([i for i in apples if (i+a>=s and i+a<=t)]))
    print(len([i for i in oranges if (i+b>=s and i+b<=t)]))
countApplesAndOranges(7,11,5,15,[-2,2,1],[5,-6])
# File: Beautiful Days at the Movies.py
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
# File: beautifulTriplets.py
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

#----------------------------------------------------------------
def beautifulTriplets(d, arr):
    count = 0
    for i in arr:
        if i + d in arr and i + 2*d in arr:
            count += 1
    return count
print(beautifulTriplets(3,[1, 2, 4, 5, 7, 8, 10]))
# File: between-two-sets.py
a,b=[2, 4], [16, 32, 96]
s=0
for i in range(max(a), min(b)+1):
		for k in a:
				if i % k != 0:
						break	
		else:
				for k in b:
						if k % i != 0:
								break
				else:
						s+=1
print(s)
# File: breaking-best-and-worst-records.py
scores=[10 ,5 ,20 ,20 ,4 ,5 ,2 ,25 ,1]
h=0
e,o=0,0
l=0
for i in range(len(scores)):
    if i==0:
        h=scores[i]
        l=scores[i]
    if scores[i]>h:
        e+=1
        h=scores[i]
    elif scores[i]<l:
        o+=1
        l=scores[i]
print(e,o)


# File: CamelCase.py
def camelcase(s):
    s = s[0].upper() + s[1:]
    c=0
    for i in range(len(s)):
        if s[i].isupper():
            c+=1
    return c
print(camelcase('saveChangesInTheEditor'))
#--------------------------------------------------------------------------
import re
def camelcase(s):
    return len(re.findall(r'[A-Z]',s))+1
		
print(camelcase('saveChangesInTheEditor'))
# File: Cats and a Mouse.py
def catAndMouse(x, y, z):
    m=max(x,y,z)
    if abs(z-y)>abs(z-x):
        return 'Cat A'
    elif abs(z-y)<abs(z-x):
        return 'Cat B'
    else:
        return "Mouse C"

print(catAndMouse(1,2,3))
print(catAndMouse(1,3,2))
print(catAndMouse(2,1,3))
# File: Circular Array Rotation.py
def circularArrayRotation(a, k, queries):
    # Write your code here
    for i in range(k):
        a.insert(0,a.pop())
    return [a[i] for i in queries]
print(circularArrayRotation([1,2,3],2,[0,1,2]))
#----------------------------------------------------------------------------------------------------
def circularArrayRotation(a, k, queries):
    # Write your code here
    return [a[(i-k)%len(a)] for i in queries]
print(circularArrayRotation([1,2,3],2,[0,1,2]))
# File: Climbing the Leaderboard.py
def climbingLeaderboard(ranked, player):
		# Write your code here
		ranked = list(set(ranked))
		ranked.sort(reverse=True)
		rank = []
		for i in player:
				while len(ranked) > 0 and i >= ranked[-1]:
						ranked.pop()
				rank.append(len(ranked)+1)
		return rank
print(climbingLeaderboard([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120]))
#---------------------------------------------------------------------------------------------------
from bisect import bisect_right as br
def climbingLeaderboard(ranked, player):
	ranked= sorted(set(ranked))
	grades= list(range(len(ranked)+1,0,-1))
	print([grades[br(ranked,i)] for i in player])
	return [(grades[br(ranked, i)]) for i in player]

print(climbingLeaderboard([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120]))
# File: Counter game.py
def counterGame(n):
    s = bin(n)
    return 'Louise' if (s.count('1') + s[:1:-1].find('1')) % 2 == 0 else 'Richard'
print(counterGame(6))
# File: Counting Valleys.py
def countingValleys(steps, path):
    u,d,c=0,0,0
    for i in path:
        if i=='U':
            u+=1
        elif i=='D':
            u-=1
        if u<0:
            d=1
        if(d==1 and u==0):
            c+=1
            d=0
    return c


print(countingValleys(12, "UDDDUDUU"))
# File: Cut the sticks.py
def cutTheSticks(arr):
    # Write your code here
    arr.sort()
    result = []
    while len(arr) > 0:
        result.append(len(arr))
        arr = [x - arr[0] for x in arr if x - arr[0] > 0]
    return result

print(cutTheSticks([1 ,2, 3, 4, 3 ,3 ,2 ,1]))
#--------------------------------------------------------------

# File: Day of the Programmer.py
def dayOfProgrammer(year):
		if year == 1918:
			return '26.09.1918'
		elif (year <= 1917 and year % 4 == 0) or (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
			return '12.09.' + str(year)
		else:
			return '13.09.' + str(year)
print(dayOfProgrammer(2017))
# File: Designer PDF Viewer.py
def designerPdfViewer(h, word):
		tallest = 0
		for letter in word:   #ord() returns the unicode of a character
				if h[ord(letter) - 97] > tallest: # ord(letter) - 97 is the index of the letter in the list
						tallest = h[ord(letter) - 97] # if the height of the letter is greater than the current tallest, set it as the tallest
		return tallest * len(word) # return the area of the word
print(designerPdfViewer([1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 1, 1, 5, 5, 1, 5, 2, 5, 5, 5, 5, 5, 5], 'zbc'))
#---------------------------------------------------------------------------------------------------
def designerPdfViewer(k,a):
		return max(k[ord(i)-97] for i in a)*len(a)
print(designerPdfViewer([1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 1, 1, 5, 5, 1, 5, 2, 5, 5, 5, 5, 5, 5], 'zbc'))
# File: diagonal-difference.py
arr=[[11, 2, 4], [4, 5, 6], [10, 8, -12]]
s=0
d=0
for i in range(len(arr)):
		s+=arr[i][i]
		d+=arr[i][len(arr)-i-1]
print( abs(s-d))	

#-------------------------------------------------------------#
s=0
d=0
for i in range(len(arr)):
		for j in range(0,i+1):
			if i==j:
				s+=(arr[i][j])
		for k in range(len(arr),0,-1):
			if i==len(arr)-k:
				d+=(arr[i][k-1])
print( abs(s-d))
# File: Drawing Book.py
def pageCount(n, p):
    if n % 2 == 0:
                n += 1
    return min(p // 2, n // 2 - p // 2)
print(pageCount(6,2))

#--------------------------------------------------------------
def pageCount(n, p):
		mid = (n >> 1)
		trg = (p >> 1) << 1
		return (mid - abs(mid - trg)) >> 1
print(pageCount(6,2))
# File: Electronics Shop.py
def getMoneySpent(keyboards, drives, b):
    l=[]
    for i in keyboards:
        for j in drives:
            if i+j<=b:
                l.append(i+j)
    if len(l)>0:
        return (max(l))
    else:
        return -1
print(getMoneySpent([3,1],[5,2,8],10))
# File: Find Digits.py
def findDigits(n):
    count = 0
    for i in str(n):
        if int(i) > 0 and n % int(i) == 0:
            count +=1
    return count

print(findDigits(1012))
# File: Flipping bits.py
def flippingBits(n):
    return n ^ 0xffffffff # 32-bit unsigned integer
print(flippingBits(802743475))
# File: Grading Students.py
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
# File: HackerRank in a String!.py
def hackerrankInString(s):
    a = 'hackerrank'
    i = 0
    for c in s:
        if i < len(a) and c == a[i]:
            i += 1
    return 'YES' if i == len(a) else 'NO'

print(hackerrankInString('rhbaasdndfsdskgbfefdbrsdfhuyatrjtcrtyytktjjt'))
# File: kangaroo.py
x1, v1, x2, v2=0 ,2,5,3
for i in range(10000):
	if x1==x2:
		print("YES")
		break
	x1+=v1
	x2+=v2
else:
	print("NO")
# File: Library Fine.py
def libraryFine(d1, m1, y1, d2, m2, y2):
    if y1 > y2:
        return 10000
    elif y1 == y2 and m1 > m2:
        return 500 * (m1 - m2)
    elif y1 == y2 and m1 == m2 and d1 > d2:
        return 15 * (d1 - d2)
    else:
        return 0
print(libraryFine(9, 6, 2015, 6, 6, 2015))
# File: Lonely Integer.py
def lonelyinteger(a):
		for i in a:
				if a.count(i)==1:
						return i
print(lonelyinteger([1, 1, 2])) # 2

#---------------------------------------------

import collections 
def lonelyinteger(a):
    a=collections.Counter(a)
    for i in a:
        if a[i]==1:
            return i
    
print(lonelyinteger([1, 1, 2])) # 2


# File: Making Anagrams.py
def makingAnagrams(s1, s2):
    # Write your code here
    s1 = list(s1)
    s2 = list(s2)
    s1.sort()
    s2.sort()
    i,j=0, 0
    count = 0
    while i < len(s1) and j < len(s2):
        if s1[i] == s2[j]:
            i += 1
            j += 1
        elif s1[i] < s2[j]:
            count += 1
            i += 1
        else:
            count += 1
            j += 1
    if i < len(s1):
        count += len(s1) - i
    if j < len(s2):
        count += len(s2) - j
    return count

print(makingAnagrams('absdjkvuahdakejfnfauhdsaavasdlkj', 'djfladfhiawasdkjvalskufhafablsdkashlahdfa'))

# File: Maximizing XOR.py
def maximizingXor(l, r):
	    return max([i^j for i in range(l,r+1) for j in range(l,r+1)])

print(maximizingXor(11,100))
#--------------------------------------------------------------

l,r=11,100
s=0
for i in range(l,r+1):
    for j in range(l,r+1):
        k=i^j
        if k>s:
            s=k
print(s)


# File: Migratory Birds.py
def migratoryBirds(arr):
    s={i:arr.count(i) for i in list(set(arr))}
    m=(max(s.values()))
    return min([k for k,v in s.items() if m==v])

print(migratoryBirds([1,4,4,4,5,3]))
# File: Picking Numbers.py
def pickingNumbers(a):
		a.sort()
		m=0
		for i in range(len(a)):
			c=0
			for j in range(i,len(a)):
				if abs(a[i]-a[j])<=1:
					c+=1
			if c>m:
				m=c
		return m

print(pickingNumbers([4, 6, 5, 3, 3, 1]))
#-------------------------------------------------------------------------------
def pickingNumbers(a):
    # Write your code here
    res=1
    for i in range (max(a)+1) :
        res=max(res,a.count(i)+a.count(i+1))
    return res
print(pickingNumbers([1, 2, 2, 3, 1, 2]))
# File: Recursive Digit Sum.py
def superDigit(n, k):
    if len(n) == 1:
        return n
    else:
        return superDigit(str(sum([int(i) for i in n]) * k), 1)
print(superDigit('148', 3))
# File: Sales by Match.py
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

s={}.fromkeys(ar,0)
for i in ar:
		s[i]+=1
print(s)
c=0
for i in s.values():
	while i>=2:
		c+=1
		i=i-2
print(c)
#----------------------------------------------------------------------#
count = 0
for x in set(ar):
	count += ar.count(x)//2
print(count)
# File: Save the Prisoner!.py
def saveThePrisoner(n, m, s):
    if (m + s - 1) % n == 0:
        return n
    else:
        return (m + s - 1) % n
print(saveThePrisoner(4,6,2))
#----------------------------------------------------------------------------------------------------
def saveThePrisoner(n, m, s):
    return (m + s - 2) % n + 1
print(saveThePrisoner(4,6,2))
# File: Sequence Equation.py
def permutationEquation(p):
    l=[]
    for i in range(1,len(p)+1):
        l.append(p.index(p.index(i)+1)+1)
    return l
    
print(permutationEquation([2,3,1]))
#---------------------------------------------------------------------------------------------------

# File: Subarray Division.py
s, d, m=[1, 2, 1, 3, 2], 3, 2
c=0
k=0
for i in range(len(s)):
	if sum(s[k:m+k])==d:
		c+=1
	k+=1
print(c)
print(sum(s[1:3]))
# File: The Hurdle Race.py
def hurdleRace(k, height):
    # Write your code 
    m=max(height)
    if m>k:
        return m-k
    else:
        return 0

print(hurdleRace(4,[1,6,3,5,2]))
# File: Two Strings.py
def twoStrings(s1, s2):
    a=set(s1) &set(s2)
    if len(a)>0:
        return 'YES'
    else:
        return 'NO'

print(twoStrings('hello','world'))

#-------------------------------------------------------------------------
def twoStrings(s1, s2):
		return 'YES' if set(s1) &set(s2) else 'NO'
print(twoStrings('hello','world'))
# File: Utopian Tree.py
def utopianTree(n):
		height = 1
		for i in range(n):
				if i % 2 == 0:
						height *= 2
				else:
						height += 1
		return height
print(utopianTree(4))

#--------------------------------------------------------------------------------------------------------------
def utopianTree(n):
    # Write your code here
    if n == 0:
        return 1
    elif n % 2 == 0:
        return (1+utopianTree(n-1))
    else:
        return (2 * utopianTree(n-1))
print(utopianTree(4))
# File: Viral Advertising.py
def viralAdvertising(n):
    shared = 5
    liked = 0
    cumulative = 0
    for i in range(n):
        liked = shared // 2
        cumulative += liked
        shared = liked * 3
    return cumulative
print(viralAdvertising(3))