import random

def print_matrix(width=10, height=10):
    for _ in range(height):
        row = random.sample(range(0, 10), width)
        for num in row:
            print(f"{num:3}", end=" ")
        print()

# Call the function to print the default 10x10 matrix
print_matrix()