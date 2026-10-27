x = int(input("Enter a number: "))

if x < 0:
    print(False)
elif str(x) == str(x)[::-1]:
    print(True)
else:
    print(False)