import os, sys

sys.path.append(os.path.abspath('./codeitsuisse/challenges'))

if __name__ == '__main__':
    challenge = sys.argv[1]
    c = __import__(challenge)

    for i in c.tests:
        print('')
        print('test_case:', i)
        print('result:   ', c.evaluate(i))
