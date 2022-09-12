# Take a number input from user and print its table

num = int(input("Enter a Number : "))

for i in range(1, 11, 1):
    print(f"{num}*{i}={num*i}")