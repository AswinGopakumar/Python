#In the party problem we would like to know how many people must be invited to a party where we can guarantee that there is a group of 3 people who either all are friends or all strangers. We want to invite the minimum number of people because would like to spend as little money as possible.
print('----------------------------------------------------------------------------------------------------------------')
print(" \n \t \t \t \t \tParty Problem \n")
print("----------------------------------------------------------------------------------------------------------------")
print("\n In the party problem we would like to know how many people must be invited to a party where we can guarantee that there is a group of 3 people who either all are friends or all strangers. We want to invite the minimum number of people because would like to spend as little money as possible. \n")
print('----------------------------------------------------------------------------------------------------------------')
print("\n Q) What is the minimum number of people that should be invited to the party to satisfy the Ramsey number R(3,3)\n")
print("""\n -> Minimum number of people required is "6" to satisfy the condition\n""")
print('----------------------------------------------------------------------------------------------------------------')

y = input("\nTo check whether the given number of people satisfy the condition enter 'Yes' Else enter 'No' \n")
while(y == "Yes") or (y == "yes"):
    a = 0
    a = input("Enter the number of people \n")
    b = int(a)
    if(b >= 6):
        print("Condition is satisfied \n")
    else:
        print("Condition is not satisfied\n")
    c = input("Do you want to check again. If yes enter 'Yes', if no enter 'No'\n")
    if(c == "no") or (c == "No"):
        break
    


