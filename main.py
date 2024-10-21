# Import necessary libraries (not used in this program but can be useful in complex scenarios)
import math
import os
import random
import re
import sys

# Function to count Apples and Oranges that fall within the house range
def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Initialize lists to store the final positions of Apples and Oranges
    apple_pos = []
    orange_pos = []
    
    # Calculate where each apple falls and store the position in the apple_pos list
    for apple in apples:
        apple_add = a + apple  # Position where apple lands = apple tree position + distance of the apple from the tree
        apple_pos.append(apple_add)  # Add the calculated position to the apple_pos list
    
    # Calculate where each orange falls and store the position in the orange_pos list
    for orange in oranges:
        orange_add = b + orange  # Position where orange lands = orange tree position + distance of the orange from the tree
        orange_pos.append(orange_add)  # Add the calculated position to the orange_pos list
    
    # Initialize counters to count how many Apples and Oranges land in the house range
    count_apple = 0
    count_orange = 0
    
    # Count apples that land in the house range [s, t]
    for apple in apple_pos:
        if s <= apple <= t:  # Check if the apple's position is within the house range
            count_apple += 1  # Increment the apple counter if the condition is true
    
    # Count oranges that land in the house range [s, t]
    for orange in orange_pos:
        if s <= orange <= t:  # Check if the orange's position is within the house range
            count_orange += 1  # Increment the orange counter if the condition is true
    
    # Print the final count of Apples and Oranges that landed in the house range
    print(count_apple)
    print(count_orange)

# Main block to get user inputs and call the function
if __name__ == '__main__':
    # Input the range of the house (s: start, t: end)
    first_multiple_input = input("Enter the start and end point of the house range (s t): ").rstrip().split()
    s = int(first_multiple_input[0])  # Start point of the house
    t = int(first_multiple_input[1])  # End point of the house

    # Input the positions of the apple tree (a) and the orange tree (b)
    second_multiple_input = input("Enter the position of the apple tree (a) and the orange tree (b): ").rstrip().split()
    a = int(second_multiple_input[0])  # Position of the apple tree
    b = int(second_multiple_input[1])  # Position of the orange tree

    # Input the number of Apples (m) and Oranges (n) thrown
    third_multiple_input = input("Enter the number of apples (m) and oranges (n): ").rstrip().split()
    m = int(third_multiple_input[0])  # Number of Apples
    n = int(third_multiple_input[1])  # Number of Oranges

    # Input the distances each apple falls from the apple tree
    apples = list(map(int, input(f"Enter the distances of {m} apples: ").rstrip().split()))

    # Input the distances each orange falls from the orange tree
    oranges = list(map(int, input(f"Enter the distances of {n} oranges: ").rstrip().split()))

    # Call the function to count how many Apples and Oranges land in the house range
    countApplesAndOranges(s, t, a, b, apples, oranges)
