#In the party problem we would like to know how many people must be invited to a party where we can guarantee that there is a group of 3 people who either all are friends or all strangers. We want to invite the minimum number of people because would like to spend as little money as possible.
import os
def problemdef():
    print('----------------------------------------------------------------------------------------------------------------')
    print(" \n \t \t \t \t \tParty Problem \n")
    print("----------------------------------------------------------------------------------------------------------------")
    print("\n In the party problem we would like to know how many people must be invited to a party where we can guarantee that there is a group of 3 people who either all are friends or all strangers. We want to invite the minimum number of people because would like to spend as little money as possible. \n")
    print('----------------------------------------------------------------------------------------------------------------')
    print("\n Q) What is the minimum number of people that should be invited to the party to satisfy the Ramsey number R(n,n)\n")
problemdef()
y = 1
while True:
    try:  
        n = int(input("\nEnter the value of n : "))
    except ValueError:
        print("Type numerical values")
        continue
    
    if n <= 1:
        print('\n->There is no solution for the given condition\n')

    elif n == 2:
        print("""\n-> Minimum number of people required is "2" to satisfy the condition\n""")

    elif n == 3:
        print("""\n-> Minimum number of people required is "6" to satisfy the condition\n""")

    elif n == 4:
        print("""\n-> Minimum number of people required is "18" to satisfy the condition\n""")

    elif n == 5:
        print("""\n-> Minimum number of people required will range from "43 - 48" to satisfy the condition\n""")

    else:
        print("\n->Solution for the given condition is not discovered yet!\n")

    print('----------------------------------------------------------------------------------------------------------------')
    a = 0
    while a == 0:
        c = input("Do you want to check again. If yes enter 'Yes', if no enter 'No'\n")
        if(c == "no") or (c == "No"):
            a = 1
            exit()
        elif c == "yes" or c == "Yes":
            a = 1
            os.system('clear')
            problemdef()
            continue

    



