'''Find the first repeated character in a string. For example, if input is "john doe", output would be "o"'''

def reapeated_char(n):
    char_set = set()                 # Create an empty set to store encountered characters
    words = n.split()                # Split input string and store it in words
    for i in words:                  # Iterate over each i in the list of words
        for char in i:               # Iterate over each character in the i
            if char in char_set:     # If the character is already in the set
                return char          # Return the character as the first repeated character
            else:
                char_set.add(char)   # Add the character to the set
    return None
                
def main():
        
        n = input("enter any string :")   # input string by user
        result = reapeated_char(n)        # caling function
        if result is not None:
            print("The first repeated character is:", result)
        else:
            print("There are no repeated characters.")

main()        

