'''Write a function that takes an email address as argument,
parses it and guesses the first and last name from the email address and returns as a tuple.
As an example, if email address is mukesh.kumar@gmail.com, the function should return (Mukesh, Kumar).'''

def Read_email(mail):
    first_part,second_part = mail.split('@')
    
    first_part = first_part.split('.')

    second_part = second_part # we have to use first part only 

    first_part = tuple(first_part)
    return first_part
def main():
    mail = input("enter the any valid email address as (name.surname@xyz.com)")
    result = Read_email(mail)
    print("The name and surname are as follows :",result)
main()
