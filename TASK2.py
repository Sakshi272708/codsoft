# Design a simple calculator with basic arithmetic operations.Prompt the user to input two numbers and an operation choice.
# Perform the calculation and display the result.
def calculator():
    while True:
        print("1.add")
        print("2.substract")
        print("3.multiply")
        print("4.divison")
        user_choice=input("enter your choice")
        a=int(input("enter first no."))
        b=int(input("enter second no."))
        if user_choice=="1":
            print(a+b)
        if user_choice=="2":
             print(a-b)
        if user_choice=="3":
           print(a*b)
        if user_choice=="4":
            print(a/b)
calculator()