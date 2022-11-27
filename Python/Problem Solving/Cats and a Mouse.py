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