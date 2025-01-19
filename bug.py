def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError:
        print("Error: Invalid data type")
        return None

# Example usage
result1 = function_with_uncommon_error(10, 2)  #Correct
print(f"Result 1: {result1}")
result2 = function_with_uncommon_error(10, 0)  #Correct
print(f"Result 2: {result2}")
result3 = function_with_uncommon_error(10, "a")  #Correct
print(f"Result 3: {result3}")
result4 = function_with_uncommon_error("abc",2) # Uncommon TypeError
print(f"Result 4: {result4}")