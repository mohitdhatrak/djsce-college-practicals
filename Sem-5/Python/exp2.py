# input - always taken in the form of a string
x = input("Enter your name: ")
y = 10
print(x, y)
print(type(x))
print()

# print - if object, then it will be converted into a string before written to the screen
# print(object(s), sep=separator, end=end, file=file, flush=flush)
# sep - default is ' '
# end - default is '\n'
# file - default is sys.stdout, which means the output will be printed to the console
# flush - default behavior (False) is generally suitable for standard use
# means that the content may not be immediately written to the file or console

# input type cast from str to whatever
x = input("Enter number: ")
print(type(x))
x = float(x)
print(x)
print(type(x))
