# length = input("Please enter the length of : ")

# print("the area of the rectangle is :", area_of_square)
# a = int(input("please enter the value of a : "))
# b = int(input("please enter the value of b : "))
# c = (a**2 + b**2)**0.5
# print(c)


# Name = "tomatos"
# Quantity = 5
# Amount = 100

# total_amount=Quantity*Amount
# print("quantity" , "name" , total_amount)

# input("please what is the name of costomer,:")

# user = "shop"
# name = ("?")
# age  = ("?")

# print("user" ,"name", age)
# input("what year will age be",)*10

# a = int(input("input a: "))
# b = int(input("input b: "))

# c = (a**2 + B**2)**0.5
# print("the value of c is :")


# a = 15
# b = 5

# print(a + b)

# name = input("name :")
# total =(name * 1000)

# print = (total)

# name = input("Please enter your full name : ")
# splitted_name = name.split() 
# first_name = splitted_name[0]
# second_name = splitted_name[1]

# print("your first name is ",first_name)
# print("your last name is ", second_name)

 
# print(f"\t(1)\t(2)\t(3)\t(4)\t(5)")
# print(f"\t(1)\t(2)\t(3)\t(4)\t(5)")

# for i in range(1,10):
#     for n in range(1,10):
#         print(f"{n+i}", end = "\t")
#     print("\n")

# for i in (1,2,3,4,5):
#     print(i)

# "ABIOLA"
# for letter in "ABIOLA":
#     print("hello")

# iter("abiola")
# print(iter "abiola"):

# count = 0

# for number in range(1000):
#     if number%2 == 0 and  number%90 == 0: 
#         print(number)
#         count = count + 1

# print(f"The total number is  : {count}")

strin = """Emma
Olivia
Ava
Isabella
Sophia
Charlotte
Mia
Amelia
Harper
Evelyn
Abigail
Emily
Elizabeth
Mila
Ella
Avery
Sofia
Camila
Aria
Scarlett
Victoria
Madison
Luna
Grace
Chloe
Penelope
Layla
Riley
Zoey
Nora
Lily
Eleanor
Hannah
Lillian
Addison
Aubrey
Ellie
Stella
Natalie
Zoe
Leah
Hazel
Violet
Aurora
Savannah
Audrey
Brooklyn
Bella
Claire
Skylar
Lucy
Paisley
Everly
Anna
Caroline
Nova
Genesis
Emilia
Kennedy
Samantha"""

# splitted_str = strin.split("\n")
# print(splitted_str)

# for name in splitted_str :
#     print(f"hello,{name}  bye {name}")  

# for name in names:
#     if name == longest_name:
#         print(longest_name)

# name = strin.split("\n")
# print(name)

# longest_name = max(len(i) for i in name)
# print(longest_name)
# for i in name:
#         if len(i) == longest_name:
#             print(i)


# name = strin.split("\n")
# position_of_name = 0
# name_inp = input("input name: ")
# for i in name:
#     position_of_name += 1
#     if i == name_inp:
#         print(f"\n{name_inp}is positioned at {position_of_name}")

# # x,y,z = input("2,4,6:")
# # sum = int(x) + int(y) + int(z)
# # print(sum)
# # if x == y == z:
# #     print(3*sum)
# # else:
# #     print(sum)m

# m = 0
# while m <= 20:
#     m += 2
#     p

# a = ['foo','bar','baz','qux','quux','corge']
# print(a[3])

# for element in a:
#     print(element)
#     a.append(element)
#     print(a)
# a+=a

# print(a)

# numbers = [x for x in range(20)]
# print(numbers)
# sliced = numbers[0:20:3]
# numbers[0:20:2] = list(range(0,30,3))
# print(numbers)



    #  Assignment Q2: Solve puzzle in attached photo
    #* Guidance used: https://mindyourdecisions.com/blog/2018/06/18/only-a-
    # mastermind-can-solve-this-puzzle/
    ! z = violet; y = white; x = blue
    * all numbers (z,y and x) must be between 1 and 9: range(0,10). therefore:
    for z in range(1,10):
        #* as 3z = z + unknown addition; unknown addition = 2z which gives a max 
    value of 18. therefore:
        for unknown_addition in range(1,19):
            if z == unknown_addition/2:
                total_addition = str(z + unknown_addition)
                #* the second digit in total_additon must be equal to z. this helps 
    in finding z (violet circle)
                if (total_addition)[-1] == str(z):
                    z_report = f'The value of the violet circle is: {z}'
                    #* as the total sum is made up of three violet circles(z), its 
    value 555 is given by:
                    total_sum = int(str(z)+str(z)+str(z))
                    #* and (3*xyz) = zzz.  therefore:
                    xyz_digit_string = str(total_sum/3)
                    #* as we now have the actual number, we can deduce y and z:
                    x = xyz_digit_string[0]
                    x_report = f'The value of the blue circle is: {x}'
                    y = xyz_digit_string[1]
                    y_report = f'The value of the white circle is: {y}'
                    print(x_report)
                    print(y_report)
                    print(z_report)


