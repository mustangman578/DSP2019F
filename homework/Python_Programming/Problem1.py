#! \usr\bin\env 'python'
my_string = 'Python is the best language for String manipulation!'

print("This is Python version 3.5.2 \n\n")
print(my_string + '\n\n')
print(my_string[::-1] + '\n\n')
print(my_string[::-2] + '\n\n')
print(my_string[:1].lower() + my_string[1:32].upper() + my_string[32].lower() +my_string[33:].upper() + 4*'\n')
print("The sentence "+"'"+my_string+"'\n""4 'a' letters, and\n""0 'A' letters!" + 2*"\n" )
print('Python\n''is\n''the\n''best\n''language\n''for\n'"Sting\n"'manipulation\n\n')
print("Python\nis\nthe\nbest\nlanguage\nfor\nSting\nmanipulation".upper())
