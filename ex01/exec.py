import sys

def main():
    print(' '.join(sys.argv[1:])[::-1].swapcase())

if __name__ == '__main__':
    main()