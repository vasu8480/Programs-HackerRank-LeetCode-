#prime 
import time
t1 = time.time()
print(t1)
def prime(a,b):
    for i in range(a+1,b):
        if i>1:
            for j in range(2,i):
                if i%j==0:
                    break
            # else:
            #     print(i)

prime(1,12554)


t2=time.time()
print(t2-t1)