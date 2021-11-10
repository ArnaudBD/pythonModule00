import sys
import locale
locale.getlocale()
locale.setlocale(locale.LC_ALL, 'C')

def main():
    if len(sys.argv) == 3:
        if sys.argv[1].isnumeric() and sys.argv[2].isnumeric():
            print("{:20} {}".format("Sum:", locale.atoi(sys.argv[1]) + locale.atoi(sys.argv[2])))
            print("{:20} {}".format("Diference:", locale.atoi(sys.argv[1]) - locale.atoi(sys.argv[2])))
            print("{:20} {}".format("Product:", locale.atoi(sys.argv[1]) * locale.atoi(sys.argv[2])))
            if locale.atoi(sys.argv[2]) != 0:
                print("{:20} {}".format("Quotien:", locale.atoi(sys.argv[1]) / locale.atoi(sys.argv[2])))
                print("{:20} {}".format("Remainder:", locale.atoi(sys.argv[1]) % locale.atoi(sys.argv[2])))
            else:
                print("{:20} {}".format("Quotien:", "ERROR (div by zero)"))
                print("{:20} {}".format("Remainder:", "ERROR (modulo by zero)"))
                print("\nUsage: python operations.py <number1> <number2>\nExample:\npython operations.py 10 3")
        else:
            print("InputError: only numbers\n")
            print("Usage: python operations.py <number1> <number2>\nExample:\npython operations.py 10 3")
    else:
        if len(sys.argv) > 2:
            print("InputError: too many arguments\n")
        print("Usage: python operations.py <number1> <number2>\nExample:\npython operations.py 10 3")

if __name__ == '__main__':
    main()