"""resume: This program use two functions to validate users and password with the compliance of some
requirements. It repite the process until the requirements are complete and it doesnt let to input 
an username already registred """

# This program need to use a special characters list, because of that I did write: import string
import string
list_user = ["R0s3l1n", "princ3ssLin", "princ3ssYuki"] #Usernames already registred (Data base)

# I did declare the function to validate_user:
def validate_user(user):
    is_valid = True # I declare valid this function if it does not enter in the following conditions

    # I did declare a variable wich contains = string.punctuation (a str with all the special characters)
    chars = string.punctuation
 
    if len(user) < 6 or len(user) > 12: #1 requirement: not less than 6 and more than 12 characters
        is_valid = False
    
    if " " in user: #2 requirement: not valid for empty espaces 
        is_valid = False

    for element in user: #3 requirement: only alphanumeric characters (not valid for special characters)
        if element in chars:
            is_valid = False

    if user in list_user: #4
        is_valid = False
    
    return is_valid 

# I declare the function to validate_password:
def validate_password(password):
    is_valid = False # I declare not valid this function if it does not enter in the following conditions

    # I did convert string.punctuation (a str with all the special characters) in a list []
    chars = string.punctuation
    list_chars = [] # This empty list will contains the special characters of string.punctuation

    for element in chars:
        list_chars.append(chars) #Create a list with every character in string.punctuation

    mayus = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", 
    "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    minus = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", 
    "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    numbers = ["0","1", "2", "3", "4", "5", "6", "7", "8", "9"]
    parameters = mayus + minus + list_chars + numbers # I did declare one requirements general list 
    
    # I did declare accumulators of each requirement to validate if password contains it
    v_minus = 0
    v_mayus = 0
    v_numbers = 0
    v_chars = 0
    
    if " " in password:
        is_valid = is_valid

    if len(password) >= 8: #1 requirement: it has to have at least one of the requirements general list
        for element in password:
            if element in mayus:
                v_mayus += 1
            elif element in minus:
                v_minus += 1
            elif element in numbers:
                v_numbers += 1
            elif element in chars:
                v_chars += 1

    if v_mayus > 0 and v_minus > 0 and v_numbers > 0 and v_chars > 0:
        is_valid = True
    
    return is_valid
    
print ("***** Create an account *****\n") #Title

#Call function validate_user

print ("Parameters: Username must contain between 6 and 12 alphanumeric characters \n")

while True: #It does not finish until meets the required parameters
    user = input ("Please introduce an username: ")
    if user in list_user:
        print ("Username already registred, please try again")
    if validate_user(user):
        list_user.append(user) #To store new usernames
        break
    else:
        print ("Enter an username that meets the required parameters")

print ("Username stablished \n") #When the username is ok!

#call function validate_password:
print ("""parameters: password must contain more than 8 characters and include at least one letter
uppercase, one special character, numbers, and lowercase letters  \n""")

while True: #It does not finish until meets the required parameters
    password = input ("Please introduce a password: ")
    if validate_password(password):
        break
    else:
        print ("Enter a password that meets the required parameters")
      
print ("Password stablished \n") #When the password is ok!

print ("Your registration has been successful") #Final message

print (list_user) #To know if the new username has been register






