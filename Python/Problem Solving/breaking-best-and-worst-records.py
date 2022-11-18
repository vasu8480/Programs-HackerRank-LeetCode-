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

