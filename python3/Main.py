
if not True:
    print("Thiago")
    print("Fonseca")
else:
    print("NOT")
    print("IN")

total = 10 + \
    10 + \
    10

print(total)

paragraph = """Hello
World"""

print(paragraph)

'''
Comments works like this
'''

# Get the input of user
#input("Waiting for an enter")


import sys; x = 'foo'; sys.stdout.write(x + '\n')


counter = 100
counterFloat = 100.99

print(counter)
print(counterFloat)

a = b = c = 1
print(a + b + c)

d, e, f = 1, 2, 3
print(d + e + f)

del d

d = 10
print(d + e + f)




str = "Hello World"

print(str)
print(str[0])
print(str[2:5])
print(str[2:])
print(str[:5])
print(str * 2)
print(str + 'TEST')


#Lists

list = ['thiago', 32, 'fonseca', 45]
tinyList = [123, 'Java']

print(list)
print(list[0])
print(list[1:3])
print(list[2:])
print(list[:3])
print(tinyList * 2)
print(list + tinyList)


#Tuples

tuple = ('thiago', 32, 'fonseca', 45)
tinyTuple = (123, 'Java')

print(tuple)
print(tuple[0])
print(tuple[1:3])
print(tuple[2:])
print(tuple[:3])
print(tinyTuple * 2)
#print(list + tinyTuple)


# Dictionaries
print("\nDictionaries")

dict = {}
dict["one"] = "This is the one"
dict[2] = "This is the number two"

directDict = {'name': "Thiago Fonseca", "department":"IT"}

print(dict)
print(dict["one"])
print(dict[2])

print (directDict)
print (directDict.keys())
print (directDict.values())



# If statements
var = 1000

if (var == 1000):
    print("THe value is correct")



myList = [1, 2, 3]

print(myList)

myList.append(4)
myList.reverse()

print(myList)


def printMe(text):
    print('Printing me: ' + text)


printMe(text = "Joselito")
