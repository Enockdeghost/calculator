# create fuction's for operation
def add(x,y):
    return x + y
def substract(x,y):
    return x - y
def multiply(x,y):
    return(x * y)
def division(x,y):
    return(x / y)

# make choice for user
print('welcome to annomy\'s calculator ')
print(" 1:addition \n 2:substract \n 3:multiply \n 4:division")
# set option after get user's answer
while True:
    # try to avoid error during user input
    try:
        choice = int(input('choose operation: '))
        if choice == 1:
            num1 = float(input('enter first number: '))
            num2 = float(input('enter second number: '))
            print(f"{num1} + {num2} = ",add(num1,num2))
        elif choice == 2:
            num1 = float(input('enter first number: '))
            num2 = float(input('enter second number: '))
            print(f"{num1} - {num2} = ",substract(num1,num2))
        elif choice == 3:
            num1 = float(input('enter first number: '))
            num2 = float(input('enter second number: '))
            print(f"{num1} * {num2} = ",multiply(num1,num2))
        elif choice == 4:
            num1 = float(input('enter first number: '))
            num2 = float(input('enter second number: '))
            print(f"{num1} / {num2} = ",division(num1,num2))

        # see's if the user's want to continue use calculator
        next = str(input('you want to continue (Y/N): ').lower())
        if next == 'y':
            continue
        else:
            print('have a nice a day')
            break
    except Exception as e:
        print("there some error:", e)