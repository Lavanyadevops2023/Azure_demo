#polindrome or not
string=input("Enter the string:")
if(string==string[::-1]):
    print("The given string is polidrome")
else:
    print("The given string is not polindrome")