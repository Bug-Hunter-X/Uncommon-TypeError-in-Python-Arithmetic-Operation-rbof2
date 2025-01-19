def function_with_uncommon_error(a, b):
    try:
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            result = a / b
            return result
        else:
            print("Error: Invalid data type. Only numbers are allowed.")
            return None
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Example usage
result1 = function_with_uncommon_error(10, 2) #Correct
print(f"Result 1: {result1}")
result2 = function_with_uncommon_error(10, 0) #Correct
print(f"Result 2: {result2}")
result3 = function_with_uncommon_error(10, "a") #Correct
print(f"Result 3: {result3}")
result4 = function_with_uncommon_error("abc",2) #Correct
print(f"Result 4: {result4}")
result5 = function_with_uncommon_error(10.5, 2.5) #Correct
print(f"Result 5: {result5}") 