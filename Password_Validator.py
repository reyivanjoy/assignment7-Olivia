# Password Validator
password_name = str(input("Enter Password: "))
letters = 0
capital_letters = 0
numbers = 0
special_characters = 0
for i in password_name:
    if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or 
    i == 'b' or i == 'c' or i == 'd' or i == 'f' or i == 'g' or 
    i == 'h' or i == 'j' or i == 'k' or i == 'l' or i == 'm' or 
    i == 'n' or i == 'p' or i == 'q' or i == 'r' or i == 's' or 
    i == 't' or i == 'v' or i == 'w' or i == 'x' or i == 'y' or 
    i == 'z' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or 
    i == 'U' or i == 'B' or i == 'C' or i == 'D' or i == 'F' or 
    i == 'G' or i == 'H' or i == 'J' or i == 'K' or i == 'L' or 
    i == 'M' or i == 'N' or i == 'P' or i == 'Q' or i == 'R' or 
    i == 'S' or i == 'T' or i == 'V' or i == 'W' or i == 'X' or 
    i == 'Y' or i == 'Z'):
        letters = letters + 1
    if(i == 'A' or i == 'E' or i == 'I' or i == 'O' or 
    i == 'U' or i == 'B' or i == 'C' or i == 'D' or i == 'F' or 
    i == 'G' or i == 'H' or i == 'J' or i == 'K' or i == 'L' or 
    i == 'M' or i == 'N' or i == 'P' or i == 'Q' or i == 'R' or 
    i == 'S' or i == 'T' or i == 'V' or i == 'W' or i == 'X' or 
    i == 'Y' or i == 'Z'):
        capital_letters = capital_letters + 1
    if(i == '0' or i == '1' or i == '2' or i == '3' or 
    i == '4' or i == '5' or i == '6' or i == '7' or 
    i == '8' or i == '9'):
        numbers = numbers + 1
    # Special Characters that are only Accepted are the Following: (. , / ! @ # $ % ^ & * ( ) _ + - =)
    if(i == '.' or i == ',' or i == '/' or i == '!' or 
    i == '@' or i == '#' or i == '$' or i == '%' or 
    i == '^' or i == '&' or i == '*' or i == '(' or
    i == ')' or i == '_' or i == '+' or i == '-' or
    i == '='):
        special_characters = special_characters + 1 

if letters > 15:
    if capital_letters >=1:
        if numbers >= 1:
            if special_characters >= 1:
                print("Password is Valid")
else:
    print("Password is Invalid")
