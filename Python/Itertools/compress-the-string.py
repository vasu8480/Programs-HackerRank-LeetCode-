from itertools import groupby

string = input()
print(' '.join( str( (len(list(g)), int(k)) ) for k,g in groupby(string)))

#-----------------------------------------------------------#
print(*[(len(list(g)), int(k)) for k, g in groupby(input())])
