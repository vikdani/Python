# Write a program to decrypt a given phrase
# The code in this case is a phrase made from the first letter of each word in the given phrase.
# Input: "his elephant licked lots of wet orange round liquid droplets"
# Output: helloworld

def phrase(n):
    phrase_set = []
    string = ''
    words = n.split()
    for w in words:
        phrase_set.append(w[0])
    output = string.join(phrase_set)
    return output
def main():
    n = input("Enter any phrase :")
    output = phrase(n)
    print("Required first letter of complete phrase :",output  )  
main()    
