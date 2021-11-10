import sys
import locale
locale.getlocale()
locale.setlocale(locale.LC_ALL, 'C')


def main():
    if len(sys.argv) != 2:
        print('Error')
        sys.exit()
    args = locale.atoi(sys.argv[1])
    if  not isinstance(args, int):
        print('Error')
    elif args == 0:
        print("I'm Zero.")
    elif args % 2 == 0:
        print("I'm Even.")
    elif args % 2 != 0:
        print("I'm Odd.")

if __name__ == '__main__':
    main()