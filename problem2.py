def find_smallest_beautiful_number(number_input):
    beautiful_num = number_input

    while True:
        if beautiful_num % number_input == 0:
            unique_digits = set(str(beautiful_num))
            
            if len(unique_digits) == 1:
                print(f"The smallest beautiful number is {beautiful_num}")
                break

        beautiful_num += 1

if __name__ == "__main__":
    number_input = int(input("Number: "))
    find_smallest_beautiful_number(number_input)