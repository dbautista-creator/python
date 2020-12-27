import random
rand_number = ()
rand_numbers = [random.randrange(1, 11, 1) for i in range(5)]
rand_number = set(rand_numbers)
print("Set 1:",str(rand_number))
rand_number2 = ()
rand_numbers2 = [random.randrange(1, 11, 1) for i in range(5)]
rand_number2 = set(rand_numbers2)
print("Set 2:",str(rand_number2))
#-------------------Now I will find the union, odd, intersection, symmetric difference----------------#
print(" Set 1 union  Set 2: ",rand_number | rand_number2)
print("Set 1 intersect Set2;  ", rand_number & rand_number2)
print("Set 1 - Set 2: ",rand_number - rand_number2)
print("Set 2 - Set1:  ",rand_number2 - rand_number)
print("Symmetric difference between Set 1 and Set 2:  ", rand_number ^ rand_number2)