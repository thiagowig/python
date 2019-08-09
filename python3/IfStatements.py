
number = 5

if number == 5:
    print("The number is 5")
else:
    print("The number ISNOT 5")


if number:
    print("The number is defined")


number = None

if number:
    print("The number is defined")
else:
    print("THE NUMBER IS NOT DEFINED")


flag = False

if not flag:
    print("NOT FLAG")

if not flag and not number:
    print("NOT FLAG AND NOT NUMBER")


print("bigger" if flag else "taller")
        