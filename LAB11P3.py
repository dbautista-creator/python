lst = []
for i in range(5):
    n = input("Enter an integer: ")
    if (n.isdecimal()):
        lst.append(int(n))
    else:
        print("Input value cannot be converted to integer")
print("Integer list:", lst)
