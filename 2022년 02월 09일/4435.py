T = int(input())

for day in range(1, T + 1):
    a, b, c, d, e, f = map(int, input().split())
    g, h, i, j, k, l, m = map(int, input().split())

    good = a * 1 + b * 2 + c * 3 + d * 3 + e * 4 + f * 10
    evil = g * 1 + h * 2 + i * 2 + j * 2 + k * 3 + l * 5 + m * 10

    if good > evil:
        print('Battle {}: Good triumphs over Evil'.format(day))
    elif good < evil:
        print('Battle {}: Evil eradicates all trace of Good'.format(day))
    else:
        print('Battle {}: No victor on this battle field'.format(day))
