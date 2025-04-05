# **Fruit Fall Range Calculator**

This project is a simple Python program that calculates how many apples and oranges land within a given range, representing a house. The apples and oranges are thrown from different trees located at specific positions, and their landing positions are calculated based on their distances from the trees.

## **Features**:

**User Input:**  The program takes user input for the house range, tree positions, and the number and distances of thrown apples and oranges.

**Position Calculation:**  The final position of each apple and orange is calculated based on its distance from the respective tree.

**Counting:** The program counts how many apples and oranges fall within the house range.

**How the Program Works**

**House Range (s, t):**  The house is defined by a start (s) and end (t) position on a one-dimensional number line.

**Tree Positions:**

**a:**  Position of the apple tree.

**b:**  Position of the orange tree.

**Fruit Falling:**

**Apples:** Each apple falls a certain distance from the apple tree.

**Oranges:** Each orange falls a certain distance from the orange tree.

The program then calculates the position where each fruit lands and checks if it falls within the house range.

Finally, the program outputs the number of apples and oranges that land within the house range.

**Code Structure**:

**Main Components:**

**Input:**  The program prompts the user to enter the following:

Start (s) and end (t) points of the house range.

Position of the apple tree (a) and the orange tree (b).

Number of apples and oranges thrown.

Distances of apples and oranges from their respective trees.

**Functionality:**

The function **countApplesAndOranges()** calculates the position of each apple and orange, then checks if they fall within the house range. It counts how many fruits land in the range and prints the results.

**Example Usage**:

Enter the start and end point of the house range (s t): 7 11

Enter the position of the apple tree (a) and the orange tree (b): 5 15

Enter the number of apples (m) and oranges (n): 3 2

Enter the distances of 3 apples: -2 2 1

Enter the distances of 2 oranges: 5 -6

**Output:**

1  # One apple lands in the house range
1  # One orange lands in the house range

**Requirements**:  **Python 3.x**

**Running the Program**:

**Clone the repository:**  git clone https://github.com/your-username/Fruit-Fall-Range-Calculator.git

**Navigate to the project directory:**  cd Fruit-Fall-Range-Calculator

**Run the Python script:**  python3 fruit_fall_range_calculator.py

**Contributing**

Feel free to submit pull requests or open issues to improve the code.

**License**:

This project is licensed under the MIT License.


