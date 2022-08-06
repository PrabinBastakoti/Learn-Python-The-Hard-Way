quantity_of_numbers =int(input("Maximum of three numbers or maximum of two numbers? Press 2 or 3 and hit enter -> "))
if quantity_of_numbers==2:
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))
    def max_of_two(x,y):
        if x>y:
            return x
        return y 
    max_number1= max_of_two(first_number,second_number)
    print(f"Maximum number among two numbers is {max_number1}.")


elif quantity_of_numbers==3:
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))
    third_number = int(input("Enter the third number: "))
    def max_of_three(x,y,z):
        if x>y and x>z:
            return x
        elif y>x and y>z:
            return y
        return z
    max_number2= max_of_three(first_number,second_number,third_number)
    print(f"Maximum number among three numbers is {max_number2}.")

