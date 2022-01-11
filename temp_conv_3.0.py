# 1st argument is temperature
# 2nd argument is start scale
# 3nd argument is out scale

print("c - Celcium\nf - Fahrenhate\nk - Kelvin\nr - Rankin\nre - Reomur\nro - Rоmer\nd - Dakil\nn - Newton")


def to_celcium():
    t = float(input('Enter temperature: '))
    scale = input('From scale: ')
    match scale:
        case 'f':
            result1 = (5 / 9 * (t - 32))
        case 'k':
            result1 = (t - 273.15)
        case 'r':
            result1 = ((t - 491.67) * 5 / 9)
        case 're':
            result1 = (t * 5 / 4)
        case 'd':
            result1 = (100 - t * 2 / 3)
        case 'n':
            result1 = (t * 100 / 33)
        case 'ro':
            result1 = ((t - 7.5) * 40 / 21)
        case 'c':
            result1 = t
        case _:
            result1 = ('Enter scale not supported')
    print(str(t) + ' °' + scale + '\n')
    prog(result1)


def prog(t):
    mode = input('To scale: ')
    match mode:
        case 'c':
            result = t
        case 'f':
            result = (t * 9 / 5 + 32)
        case 'k':
            result = (t + 273.15)
        case 'r':
            result = ((t + 273.15) * 5 / 9)
        case 're':
            result = (t * 4 / 5)
        case 'ro':
            result = (t * 21 / 40 + 7.5)
        case 'n':
            result = (t * 33 / 100)
        case 'd':
            result = ((100 + t) * 3 / 2)
        case _:
            result = ('Output scale not supported')
    print(str(result) + ' °' + mode)


to_celcium()

input('Press any key')
