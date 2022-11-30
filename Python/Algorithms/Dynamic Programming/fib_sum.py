#dynamic programming bottom up
cache = {}
def fibonacci(n):
    cache[0] = 0
    cache[1] = 1

    for i in range(2, n + 1):
        cache[i] = cache[i - 1] +  cache[i - 2]

    return cache[n]
print(fibonacci(10000))
#-----------------------------------------------------------------------------------------------------

def fibonacci(n):
  a = 0
  b = 1
  for i in range(2, n + 1):
      fi = b + a
      b, a = fi, b
  return fi

print(fibonacci(10000))