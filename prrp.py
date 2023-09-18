'''input = [0,1,1,0,0,0,1,1,0,1]
output= [1,0,0,1,1,1,0,0,1,0]
hint:- covert all zero to one 
and all one to zero without using IF condition, 
you can use loop to iterate.'''

inp = [0,1,1,0,0,0,1,1,0,1]

i = 0
while i<len(inp):
    if inp[i] == 0:
        inp[i] = 1
    else:
        
        inp[i] = 0
    i = i + 1
print(inp)            