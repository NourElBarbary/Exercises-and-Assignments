from calc import add, sub, mult, div

def main():
    while True:
        command = input("Enter a command ('add', 'sub', 'mult', 'div') or 'stop' to exit: ").strip().lower()
        
        if command == "stop":
            print("Exiting the calculator. Goodbye!")
            break
        
        if command not in ("add", "sub", "mult", "div"):
            print("Invalid command. Please try again.")
            continue
        
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue
        
        if command == "add":
            result = add(num1, num2)
        elif command == "sub":
            result = sub(num1, num2)
        elif command == "mult":
            result = mult(num1, num2)
        elif command == "div":
            result = div(num1, num2)
        
        print(f"Result is: {result}")
        
        again = input("Would you like to perform another operation? (yes/stop): ").strip().lower()
        if again == "stop":
            print("Exiting the calculator. Goodbye!")
            break

if __name__ == "__main__":
    main()
