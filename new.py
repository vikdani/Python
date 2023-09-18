def van(n):
    seq  = [0] * n
    last = {}
    for i in range(1,n):
        if seq[i-1] in last:
            seq[i] = i-1- last[seq[i-1]]
        last[seq[i-1]] = i-1
    return seq
def main():
    num = int(input("enter num"))
    seq1 = van(num)
    print(seq1)
main()            

