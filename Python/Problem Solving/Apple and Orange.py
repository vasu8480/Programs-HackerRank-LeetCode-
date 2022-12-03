def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    print(len([i for i in apples if (i+a>=s and i+a<=t)]))
    print(len([i for i in oranges if (i+b>=s and i+b<=t)]))
countApplesAndOranges(7,11,5,15,[-2,2,1],[5,-6])