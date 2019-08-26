### Problem 1:
# Create a function that will ask the user for a number.
# Use the function to get two numbers from the user, then pass the two numbers to a function.
# Add, subtract, multiple, and divide the numbers.
# userInput1 = input("Enter a num ")
# userInput2 = input("Enter another num ")
a = int(input("enter first number: "))
b = int(input("enter second number: "))


def addNum():
    sum = a + b
    print(sum)

def subNum():
    sum = a - b
    print(sum)

def divNum():
    sum = a / b
    print(sum)

def mulNum():
    sum = a * b
    print(sum)

def main():
    addNum()
    subNum()
    divNum()
    mulNum()


main()
