max = 0
for i in range(0,len(accounts)):
    row = 0
    for j in range (0,len(accounts[i])):
        row = row + accounts[i][j]
    if row>max:
        max = row    

return max