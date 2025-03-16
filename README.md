# Quadratic Equation Solver

This Python script calculates the roots of a quadratic equation (ax² + bx + c = 0) based on user-provided coefficients a, b, and c.

## How to Use

1.  **Prerequisites:**
    * Python 3.x installed on your system.
2.  **Run the script:**
    * Save the code as a `.py` file (e.g., `quadratic_solver.py`).
    * Open a terminal or command prompt.
    * Navigate to the directory where you saved the file.
    * Execute the script by running the command: `python quadratic_solver.py`
3.  **Input:**
    * The script will prompt you to enter the values of `a`, `b`, and `c` one by one.
    * Enter the values and press Enter after each entry.
4.  **Output:**
    * The script will calculate and display the roots of the quadratic equation.
    * It will handle three cases:
        * Two distinct real roots.
        * One real root (repeated root).
        * Two complex roots.

## Example
Enter the value of a: 1
Enter the value of b: -3
Enter the value of c: 2
Root 1: 2.0
Root 2: 1.0

## Code Explanation

The script performs the following steps:

1.  **Input:** Takes the coefficients `a`, `b`, and `c` as input from the user.
2.  **Calculations:**
    * Calculates the discriminant (b² - 4ac).
    * Calculates the square root of the discriminant.
    * Calculates the denominator (2a).
3.  **Root Calculation:**
    * Uses conditional statements to determine the type of roots based on the discriminant.
    * Calculates the roots using the quadratic formula.
4.  **Output:**
    * Prints the calculated roots to the console.

## Dependencies

* `math` module (standard Python library). No additional installations are required.
