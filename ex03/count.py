import sys
import string

def text_analyzer(s):
    n_upper = 0
    n_lower = 0
    n_punct = 0
    n_space = 0
    n = 0
    for a in s:
        n += 1
        if a.isupper():
            n_upper += 1
        elif a.islower():
            n_lower += 1
        elif a in string.punctuation:
            n_punct += 1
        elif a == ' ':
            n_space += 1
    print("The text contains", n, "characters")
    print(n_upper, "upper letters")
    print(n_lower, "lower letters")
    print(n_punct, "punctuation marks")
    print(n_space, "spaces")


# def main():
#     text_analyzer(sys.argv[1])

if __name__ == '__main__':
    main()