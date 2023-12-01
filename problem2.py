def smallest_beautiful_number(x):
    beautiful_number = x
    while True:
        if all(digit == str(x) for digit in str(beautiful_number)):
          beautiful_number = beautiful_number + 1

        return beautiful_number

x = int(input("Input x: "))
result = smallest_beautiful_number(x)

print(f"The smallest beautiful number divisible by {x} is {result}.")