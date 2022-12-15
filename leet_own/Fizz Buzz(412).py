class Solution:
    def fizzBuzz(self, n):
        l=[]
        for i in range(1,n+1):
            if i%15==0:
                l.append("FizzBuzz")
            elif i%3==0:
                l.append("Fizz")
            elif i%5==0:
                l.append("Buzz")
            else:
                l.append("{}".format(i))
        return l
print(Solution().fizzBuzz(15))
#-----------------------------------------------------------------------------------------------------------------------
class Solution:
    def fizzBuzz(self, n):
        return [str(i) if i % 3 and i % 5 else 'Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0) for i in range(1, n + 1)]
print(Solution().fizzBuzz(15))