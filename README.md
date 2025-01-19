# Uncommon TypeError in Python Arithmetic Operations

This repository demonstrates an uncommon TypeError that can occur in Python when performing arithmetic operations on incompatible data types.  The example shows how trying to divide a string by an integer (or vice-versa) leads to this error.  The solution includes improved error handling to gracefully manage such situations. 

## Code Description

The `bug.py` file contains a Python function that attempts to divide two numbers. This function includes basic error handling for common exceptions like `ZeroDivisionError` and `TypeError`. However, it does not fully address all possible type errors that can occur. 

The `bugSolution.py` file provides a solution that handles the uncommon TypeError where the code attempts to divide a string by an integer or vice-versa using type checking and more robust error handling.