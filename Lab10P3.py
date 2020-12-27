w = open("water.txt", "w")
for i in range(4):
    number = int(input("Enter account number: "))
    customer_type = input("Enter R for residential, B for business: ")
    gallons = int(input("Enter number of gallons used: "))
    w.write(str(number) + " " + customer_type + " " + str(gallons) + "\n")
w.close()