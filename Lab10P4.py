w = open("water.txt", "w")
for i in range(4):
    number = int(input("Enter account number: "))
    customer_type = input("Enter R for residential, B for business: ")
    gallons = int(input("Enter number of gallons used: "))
    w.write(str(number) + " " + customer_type + " " + str(gallons) + "\n")
w.close()

f = open("water.txt", "r")
for line in f:
    words = line.strip().split()
    number = words[0]
    customer_type = words[1]
    gallons = int(words[2])
    charge = 0
    if customer_type == "R":
        if gallons <= 6000:
            charge = gallons * 0.005
        else:
            charge = (6000 * 0.005) + ((gallons-6000) * 0.007)
    else:
        if gallons <= 8000:
            charge = gallons * 0.006
        else:
            charge = (8000 * 0.006) + ((gallons-8000) * 0.008)
    print("Account number: %s Water charge: $%.2f" % (number, charge))
f.close()