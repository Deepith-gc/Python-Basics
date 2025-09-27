# n = int(input('Enter the number of elements in the array:').strip())
# arr = list(map(int, input('Enter the elements: ').rstrip().split()))
#
# if len(arr) == n:
#     print('Original array:', arr)
#     arr.reverse()
#     print('Reversed array:', arr)
#     print(' '.join(map(str, arr)))


# Ask the user how many numbers they want to enter
n = int(input("How many numbers do you want to enter? "))

# Ask the user to enter the numbers on one line, separated by spaces
print("Enter", n, "numbers separated by spaces:")
user_input = input()

# Convert the input string into a list of integers
arr = user_input.split()  # This gives a list of strings
arr = [int(x) for x in arr]  # Convert each string to an integer

# Check if the user entered exactly n numbers
if len(arr) != n:
    print("Oops! You entered", len(arr), "numbers instead of", n)
else:
    # Create a new list to store the reversed numbers
    reversed_arr = []

    # Add the numbers to the new list in reverse order
    for i in range(n - 1, -1, -1):
        reversed_arr.append(arr[i])

    # Print the reversed list as space-separated numbers
    print("Reversed array:")
    for num in reversed_arr:
        print(num, end=' ')


# Ask the user how many numbers they want to enter
n = int(input("How many numbers do you want to enter? "))

# Ask the user to enter the numbers on one line, separated by spaces
print("Enter", n, "numbers separated by spaces:")
user_input = input()

# Convert the input string into a list of integers
arr = user_input.split()  # This gives a list of strings
arr = [int(x) for x in arr]  # Convert each string to an integer

# Check if the user entered exactly n numbers
if len(arr) != n:
    print("Oops! You entered", len(arr), "numbers instead of", n)
else:
    # Create a new list to store the reversed numbers
    reversed_arr = []

    # Add the numbers to the new list in reverse order
    for i in range(n - 1, -1, -1):
        reversed_arr.append(arr[i])

    # Print the reversed list as space-separated numbers
    print("Reversed array:")
    for num in reversed_arr:
        print(num, end=' ')
