def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

if __name__ == "__main__":
    print(f"Add: {add(10, 5)}")
    print(f"Subtract: {subtract(10, 5)}")
    try:
        print(f"Divide: {divide(10, 5)}")
    except ValueError as e:
        print(e)