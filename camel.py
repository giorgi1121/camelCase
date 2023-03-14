#create variable
camel = input("Write some text in camelCase: ").strip()

#create empty list
letters = []

#iteration which checks every charachter in variable
for char in camel:
    #add every character to emprty list
    letters.append(char)
    
    #iteration checks index of letters in variable camel
    for i in range(len(letters)):
        #if letter with index i is capital leter, 
        #then it will be changed into lower with "_"
        if letters[i].isupper():
            letters[i] = "_" + letters[i].lower()
        
        #convert letters list into string
        string = "".join(letters)
        
    #check if first letter is upper, then remove first "_"
    if camel[0].isupper():
        new_string = string[1:]
    else:
        new_string = string
print(new_string)
