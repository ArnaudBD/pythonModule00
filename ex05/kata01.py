import sys

def main():
    languages = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
    }
    for k in languages.keys():
        print("{} was created by {}".format(k, languages[k]))

if __name__ == '__main__':
    main()
