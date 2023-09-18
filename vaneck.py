# program to print van eck sequence
def van_eck_seq(n):
    last_occurence = {}
    sequence = [0] * n
    for i in range(1,n):
        if sequence[i-1] in last_occurence:                          
                     
            difference = i-1 -last_occurence[sequence[i-1]]
            sequence.append(difference)    
        else:
            sequence.append(0)

        last_occurence[sequence[i-1]] = i - 1
    return sequence 
def main():       
    num = int(input("enter num upto which u want to print v.e.sequence :"))
    result =van_eck_seq(num)
    print(result)
main()    
