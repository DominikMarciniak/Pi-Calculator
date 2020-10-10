import random

def pi(numer_of_tests):
    points_in_circle = 0
    all_points = 0
    for x in range(numer_of_tests):
        a = random.uniform(0, 1)
        b = random.uniform(0, 1)
        if a**2 + b**2 <= 1:
            points_in_circle += 1
        all_points += 1

    Pi = 4/(all_points/points_in_circle)

    print('Pi = ', Pi)


while True:
    c = int(input('Number of tests: '))
    pi(c)
    while True:
        d = input('Try again? (Y/N): ')
        if d not in {'Y', 'y', 'N', 'n'}:
            print('Incorrect answer')
        elif d is 'N' or d is 'n':
            quit()
        else:
            break