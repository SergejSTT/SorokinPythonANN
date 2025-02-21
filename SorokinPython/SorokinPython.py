def check_number():
    print("Checking number...") 
    num = int(input("Enter a number: "))
    if num > 7:
        print("Hello")
    else:
        print("Number is not greater than 7")

def check_name():
    print("Checking name...")  
    name = input("Enter your name: ")
    if name == "John":
        print("Hello, John")
    else:
        print("There is no such name")

def check_multiples_of_3():
    print("Checking multiples of 3...")  
    numbers = list(map(int, input("Enter a list of numbers (separated by spaces): ").split()))
    print("Numbers divisible by 3:")
    for number in numbers:
        if number % 3 == 0:
            print(number)


check_number()
check_name()
check_multiples_of_3()


print("programm complieted.")
input("press any key. . .")