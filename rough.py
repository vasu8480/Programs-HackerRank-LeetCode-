def findDigits(n):
    count = 0 
    num = n 
    while(num>0): 
      dig = num%10 
      if dig > 0 and n%dig == 0: 
        count=count+1 
        num = num//10
    return count
    for i in str(k):
        if int(i) > 0 and k % int(i) == 0:
            count +=1
    return count

print(findDigits(1012))