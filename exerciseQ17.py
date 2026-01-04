import random
# Create a list with 8 random integers between 1 and 100
numbers = [random.randint(1, 100) for _ in range(8)]
print("List of numbers:", numbers)

# a) Find the biggest number using max()
biggest = max(numbers)
print("Biggest number:", biggest)

# b) Find the smallest number without using min()
# Start by assuming the first number is the smallest
smallest = numbers[0]

# Loop through the list to find the smallest
for num in numbers:
    if num < smallest:
        smallest = num

print("Smallest number:", smallest)
