def reverse(str):
    string = ''
    for i in str:
        string = i + string
    return string

print(reverse('hello whats your name'))



def reverse_string(str):
   str = str[::-1]
   return str
print(reverse_string('hello'))