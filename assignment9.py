#exception

#QS1

def compute_division():
    try:
        result = 5 / 0
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("This block always executes, whether there is an exception or not.")
compute_division()
