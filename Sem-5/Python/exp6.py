# sorting numbers

print("Enter 5 numbers:")
list1 = list()
fileWrite = open("file1.txt", "w")

for i in range(5):
    x = int(input(f"Enter number {i+1}: "))
    list1.append(x)
    fileWrite.write(str(list1[i]))
    fileWrite.write("\t")

fileWrite.close()

fileRead = open("file1.txt", "r")
list2 = list()
f = fileRead.read()
f = f.split("\t")

for j in range(len(f) - 1):
    list2.append(int(f[j]))

list2.sort()

fileWrite2 = open("file2.txt", "w")

for k in list2:
    fileWrite2.write(str(k))
    fileWrite2.write("\t")

fileWrite2.close()

fileRead2 = open("file2.txt", "r")

for x in fileRead2:
    print(x)

# sorting text

fileWrite = open("file3.txt", "w")
fileWrite.write("Hello, my name is Mohit 07 and I like Football.")
fileWrite.close()

fileRead = open("file3.txt", "r")
li = list()
f = fileRead.read()
f = f.split()

for word in f:
    li.append(str(word))

li.sort(key=lambda item: (item, len(item)))

print("List of sorted words: ")
print(li)

fileWrite2 = open("file4.txt", "w")

for i in range(len(li)):
    fileWrite2.write(str(li[i]))
    fileWrite2.write(" ")
fileWrite2.close()
