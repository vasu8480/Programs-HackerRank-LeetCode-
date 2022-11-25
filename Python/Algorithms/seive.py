#seive of eratosthenes
def sieve(n):
		if n<=2: # if n is less than 2, return empty list
			return [] #no prime numbers
		is_prime = [True] * n #create a list of booleans
		is_prime[0] = False # 0 is not prime
		is_prime[1] = False # 1 is not prime

		for i in range(2, int(n**0.5)+1):
			x = i*i  #multuiples of i are not prime
			while x < n: 
				is_prime[x] = False 	
				x += i 

		return [i for i in range(n) if is_prime[i] ] 	

		

print(sieve(12554))  # runtime 0.0009970664978027344
