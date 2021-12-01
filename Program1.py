string_name = str(input("Enter a sentence of your choice:"))
vowels = 0
consonants = 0
spaces = 0
for i in string_name:
    if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or 
    i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
        vowels = vowels + 1
    else:
        if(i == 'b' or i == 'c' or i == 'd' or i == 'f' or i == 'g' or 
    i == 'h' or i == 'j' or i == 'k' or i == 'l' or i == 'm' or i == 'n' or i == 'p' 
    or i == 'q' or i == 'r' or i == 's' or 
    i == 't' or i == 'v' or i == 'w' or i == 'x' or i == 'y' or i == 'z' or i == 'B' 
    or i == 'C' or i == 'D' or i == 'F' or 
    i == 'G' or i == 'H' or i == 'J' or i == 'K' or i == 'L' or i == 'M' or i == 'N' 
    or i == 'P' or i == 'Q' or i == 'R' or 
    i == 'S' or i == 'T' or i == 'V' or i == 'W' or i == 'X' or i == 'Y' or i == 'Z'):
            consonants = consonants + 1
        else:
            if(i == " "):
                spaces = spaces + 1
words = spaces + 1
print(f"The number of vowels is: {vowels}")
print(f"The number of consonants is: {consonants}")
print(f"The number of words is: {words}")