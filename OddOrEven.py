# Program that ask the user for a number. 
# Depending on whether the number is even or odd, 
# print out an appropriate message to the user

def main():
    try:
        userNum = int(input("Please enter a number: ")) # get user's input
                            # catch if user input is incorrect
        print("The number is odd" if userNum % 2 else "The number of even") # print out correct statement 
        print('Number is multiple of 4' if userNum % 4 == 0 else '\n') # determine if user's number is mutiple of 4...display message accordingly. 
        print("Enter two number and I will determine if they divide evenly into each other.")
        # get two integers from the user
        num1 = int(input("Enter the numerator: "))
        num2 = int(input("Enter the denominator: "))
        print(str(num1),'divdes evenly into', str(num2) if num1 % num2 == 0 else 'There is a remainder') 
    except TypeError as e:
        print(str(e))
    except ZeroDivisionError as e:
        print(str(e))
    
main()
