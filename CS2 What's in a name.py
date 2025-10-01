import random                                                   #imports random

def reverse_string(name):                                       #defines function to reverse the name                                                               
    '''
    Takes a string and reverses it
    Args:
        name(string): User's inputed name
    Returns:
        reversed string
    '''
    return name[::-1]                                           #returns reveresed string                                
    
def count_vowels(name):                                         #defines function to count vowels 
    '''
    Takes a string and returns the number of vowels in it
    Args:
        name(string): User's inputed name
    Returns:
        the total    
    '''
    vowels = ['a', 'e', 'i', 'o', 'u']                          #defines the vowels to look for
    total = 0                                                   #total amount to start counting

    for char in name:                                           #for loop
        if char in vowels:                                      #if character is a vowel
            total += 1                                          #add one to the total
    return total                                                #return the total integer amount

def count_consonant(name):                                      #defines funtion to count consonants
    '''=
    Takes a string and returns the number of consonant in it
    Args:
        name(string): User's inputed name
    Returns:
        the total    
    '''
    consonant = ['b', 'c', 'd', 'f', 'g','h','j', 'k', 'l', 'm','n','p','q', 'r', 's', 't', 'v','w','x', 'y', 'z',]     #defines the consonants to look for
    total = 0                                                  #starting amount of consonants

    for char in name:                                          #for loop
        if char in consonant:                                  #if character is a consonants
            total += 1                                         #add one to the total
    return total                                               #return the total intege amount

def my_split(name):                                            #defines split function
    '''
    Splits a name at the space
    Args:
        name(string): User's inputed name
    Returns:
        the parts of the split name
    '''

    parts = []                                                 #creates new called named parts
    current = ""                                               #defines current as an empty variable
    for char in name:                                          #for every character in name
        if char == " ":                                        #if the char is a space
            if len(current) > 0:                               #if length of current is greater than 0 
                parts.append(current)                          #add parts to current
                current = ""                                   #defines current as an empty variable
        else:                                                  #else
            current += char                                    #add current name to characters
    if len(current) > 0:                                       #if length of current is greater than zero 
        parts.append(current)                                  #add parts to current
    return(parts)                                              #then return the list of parts

def get_initials(name):                                        #defines function to get initials
    '''
    Takes a name and returns the initials
    Args:
        name(string): User's inputed name
    Returns:
        the initials
    '''
    names = my_split(name)                                     #split name at the space
    initials = ""                                              #defines initials as an empty variable

    for letter in names:                                       #for each letter in name
        initials += letter[0].upper() + ". "                   #add to varible of initials the first variable and convert it to uppercase 
    return initials                                            #return initials to function 

def return_firstname(name):                                    #defines function to return first name
    '''
    Takes a string and isolates the first name then returns it
    Args:
        name(string): User's inputed name
    Returns:
        return middle(string): seperated first name from full name   
    '''
    beg = 0                                                #beginning total is 0
    for i in range(0, len(name)):                          #for loop in characters from 0 to the end of the inputed name
        if name[i] == ' ':                                 #if space is found
            beg +=1                                        #add one to total of beg
            break                                          #break
        else:                                              #Else
            beg = beg+1                                    #add one to beginning
    first = name[: beg]                                    #first name is equal to name from beginning till the found space
    return first                                           #return first name

def return_middlename(name):                               #defines function to return first name
    '''
    Takes a string and deletes the first and last name then returns the middle
    Args:
        name(string): User's inputed name
    Returns:
        return middle(string): seperated middle name from full name   
    '''
    space = 0                                              #defines space as 0
    for char in name:                                      #for each character in name
        if char == " ":                                    #if character is a space
            space +=1                                      #add one to space 
    if space <= 1:                                         #if space  is less than 1
        middle = "No middle name"                          #tell user they have no middle name 
    else:                                                  #else 
        beg = 0                                            #set variable beg to 0
        end = len(name)-1                                  #set variable of end to length of name and to work backwards to beginning
        for i in range(0, len(name)):                      #for element in the range of 0 to the length of name
            if name[i] == ' ':                             #if name of element is a space 
                beg +=1                                    #then add 1 to beg
                break                                      #break
            else:                                          #else 
                beg = beg+1                                #add one to beg
 

        for i in range(len(name)-1,-1,-1):                 #for element in range of length of name working in reverse order 
            if name[i] == ' ':                             #checks if name has a space
                break                                      #break
            else:                                          #or else
                end = end-1                                #subtract 1 from variable end 
        middle = name[beg:end]                             #define middle, the variable, as name from beginning to end
        return middle                                      #return middle name

def return_lastname(name):
    '''
    Takes a string and isolates the last name then returns it
    Args:
        name(string): User's inputed name
    Returns:
        return last(string): seperated last name from full name   
    '''
    for i in range(len(name)-1,-1,-1):                     #for element in range of length of name working in reverse order 
        if name[i] == ' ':                                 #if name has a space
            break                                          #break
        else:                                              #else 
            end = end-1                                    #subtract 1 from end 
    last = name[: end]                                     #define variable last as name from end
    
    return last                                            #return last 

def check_hyphen(name):                                    #defines funtion to find hyphen in name
    '''
    Takes a string and isolates the hyphen from the name, then counts them
    Args:
        name(string): User's inputed name
    Returns:
        return hyphen(integer): number of hyphens in full name
    '''
    hyphen = 0                                             #set hyphen count at 0
    for letter in name:                                    #for each letter in name 
        if letter == "-":                                  #if letter is a hyphen 
            hyphen +=1                                     #add one to hyphen count 
            break                                          #break
    
    return hyphen                                           #return hyphen count 

def shuffle_name(name):                                     #define function to shufle name 
    output = []                                             #set output as a list
    while(len(name))>0:                                     #while length of name is greater than 0
        name = list(name)                                   #turn name into a list
        length = int(len(name))                             #turn variable length into integer
        length -= 1                                         #subract 1 from length
        r = random.randint(0,length)                        #find a random character within name 
        output.append(name[r])                              #add that character to output list
        name.remove(name[r])                                #then remove that character from name
    result = ""                                             #create empty string result 
    for letter in output:                                   #for each letter in output list
        result += str(letter)                               #turn it into a string and add it to result 
    return result                                           #return result

def convert_lowercase(name):                                #define function to convert name to lowercase 
    '''
    Takes a name and converts it to lowercase
    Args:
        name(string): User's inputed name
    Returns:
        the name in all lowercase letters
    ''' 
    lowered_name = ""                                       #create empty string
    for letter in name:                                     #for loop 
        num = ord(letter)                                   #convert letter to integer
        if num > 64 and num < 91:                           #if number is greater than 64 and less than 91 
            num = num + 32                                  #add 32 to that integer
            letter2 = chr(num)                              #convert integer back to lettre
            lowered_name = lowered_name + letter2           #add it to empty string
        else:                                               #or else 
            lowered_name = lowered_name + letter            #add letter to lowered name 
    return lowered_name                                     #return lowered name

def convert_uppercase(name):                                #define funciton to convert name to uppercase
    '''
    Takes a name and converts it to uppercase
    Args:
        name(string): User's inputed name
    Returns:
        the name in all uppercase letters
    ''' 
    upper_name = ""                                         #create empty string
    for letter in name:                                     #for loop
        num = ord(letter)                                   #convert letter to integer
        if num > 96 and num < 123:                          #if number is greater than 96 and lesss than 123 
            num = num - 32                                  #subtract 32 from that integer
            letter2 = chr(num)                              #convert integer to letter
            upper_name = upper_name + letter2               #add letter to lowered name
        else:                                               #else 
            upper_name = upper_name + letter                #add letter to upper name
    return upper_name                                       #return upper name

def is_palindrome(name):                                    #check if name is a palindrome
    '''
    Takes a string and checks whether it is a palindrome
    Args:
        name(string): User's inputed name
    Returns:
        name if it is a palindrome
    '''

    return name == reverse_string(name)                    #return name if reversed string of name is the same as name 

def title_distinction(name):                               #define function
    '''
    Takes a string and checks whether it is has one of the defined title
    Args:
        name(string): User's inputed name
    Returns:
        A boolean whether it contains one of the title distinctions or not
    '''

    titles = ["Dr.","Sir","Mr.","Mrs.","Esq.","Ph.d","Professor","President"]  #define titles 
    names = my_split(name)                                 #set variable names equal if finds a space 
    if names[0] in titles:                                 #if first element of names is a title
        return True                                        #return true
    else:                                                  #else 
        return False                                       #return false

def sort_letters(name):                                    #define function
    '''
    Takes a string sorts letter alphabetically
    Args:
        name(string): User's inputed name
    Returns:
        the sorted name alphabetically
    '''

    new_name = convert_lowercase(name)                      #set variable name to lowercased name                            
    new_name = []                                           #set newname as empty list
    for i in name:                                          #for loop
        new_name.append(i)                                  #add character to list new_name
    
    new_name = convert_lowercase(name)                      #set newname as coverted lowercase of name 
    return (sorted(new_name))                               #return sorted letters of new name
        
def encrypt(name):                                          #define function
    '''
    Takes a string(name) and encrypts the name by converting the letters
    Args:
        name(string): User's inputed name
    Returns:
        the letters of name converted to different letters
    '''

    name = convert_lowercase(name)                          #convert name to lowercase 
    letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]     #set letter to alphabetical letter
    cipher = ["d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c"]      #set the cipher for letter
    new_name = []                                           #create empty list
    for char in name:                                       #for loop
        num = letters.index(char)                           #convert letters to index copmparing location of a letter in one list to another 
        new_name.append(cipher[num])                        #add cipher of letter to list
    
    return new_name                                         #return the new name

def unencrypt(name):                                        #define function 
    '''
    Takes a string(name) and decrypts the name by converting the letters
    Args:
        name(string): User's inputed name
    Returns:
        the letters of name reconverted to the original letters
    '''

    name = convert_lowercase(name)                          #convert name to lowercase 
    letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]     #set letters to all letter in alphabet
    cipher = ["x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w"]      #set cipher as all letter moved over 3 places 
    new_list = []                                           #create empty list 
    for char in name:                                       #for loop 
        num = cipher.index(char)                            #convert letters to index copmparing location of a letter in one list to another
        new_list.append(letters[num])                       #add the unencryped cipher of letter to list

    return new_list                                         #return the new_list

def main():                                                 #define function
    while True:                                             #forever loop 
        word = input("Please enter your name or word")      #asks user for their name
        option = input('''                                  
                    What would you like to do?
                    1. Reverse and display name
                    2. Determine the number of vowels 
                    3. Determine the number of consonants 
                    4. Get the initials
                    5. Print First Name 
                    6. Print Middle Name 
                    7. Print Last Name
                    8. Determine number of hyphens
                    9. Shuffle name
                    10. Convert name to lowercase
                    11. Convert name to uppercase
                    12. Check if name is a palindrome
                    13. Check if name has a title distinction
                    14. Order letters in name alphabetically
                    15. Encrypt name
                    16. Decrypt name
                    17. Exit''')
        if option == "1":                               #if user chooses 1
            print(reverse_string(word))                 #print reverse_string function
        elif option == "2":                             #if user chooses 2
            print(count_vowels(word))                   #print count the amount of vowels function
        elif option == "3":                             #if user chooses 3
            print(count_consonant(word))                #print count consonants function
        elif option == "4":                             #if user chooses 4
            print(get_initials(word))                   #print get initials function  
        elif option == "5":                             #if user chooses 5
            print(return_firstname(word))               #print  only first name function
        elif option == "6":                             #if user chooses 6
            print(return_middlename(word))              #print only middle name function
        elif option == "7":                             #if user chooses 7
            print(return_lastname(word))                #print only last name function
        elif option == "8":                             #if user chooses 8
            print(check_hyphen(word))                   #print check_hyphen function
        elif option == "9":                             #if user chooses 9
            print(shuffle_name(word))                   #print shuffle name function
        elif option == "10":                            #if user chooses 10
            print(convert_lowercase(word))              #print convert lowercase function
        elif option == "11":                            #if user chooses 11
            print(convert_uppercase(word))              #print convert uppercase function
        elif option == "12":                            #if user chooses 12
            print(is_palindrome(word))                  #print check if name is palindrome function
        elif option == "13":                            #if user chooses 13
            print(title_distinction(word))              #print title_distinction function
        elif option == "14":                            #if user chooses 14
            print(*sort_letters(word))                  #print sort letters in name function
        elif option == "15":                            #if user chooses 15
            print(*encrypt(word))                       #print encrypt name function
        elif option == "16":                            #if user chooses 16
            print(*unencrypt(word))                     #print decrypt name function
        elif option == "17":                            #if user chooses 17
            break                                       #break 
        else:                                           #else
            print("Invalid Response")                   #print invalid response 
main()                                                  #call main function