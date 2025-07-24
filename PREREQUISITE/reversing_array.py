def simple_reverse(string):
    new_string = []
    for i in range(len(string)-1, -1, -1): #The for loop runs from the last element to the first element of the original string
        print(string[i])
        new_string.append(string[i]) #The characters of the original string are added to the new string
    return ''.join(new_string) #The characters of the reversed array are joined to form a string

string = "Hello"
print(simple_reverse(string))