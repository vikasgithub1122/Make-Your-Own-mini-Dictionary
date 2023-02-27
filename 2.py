my_dict= {}
for i in range(97, 97+26):
    #  ASCII values
    my_dict[chr(i)]=i
print(my_dict)


print("-----Or----")


my_dict = {chr(i): i for i in range(97, 97 + 26)}
print(my_dict)


print("-------------------")


a='a'
my_dict= {}
for i in range(ord(a), ord('z')+1):
    #  ASCII values
    my_dict[chr(i)]=i
print(my_dict)
