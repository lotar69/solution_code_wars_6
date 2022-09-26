# function name has been changed for avoiding google search cheats ;)

def changed(n):
    divisors = [1, 10, 9, 12, 3, 4]
    while len(divisors) <= len(str(n)):
        divisors += divisors
    n_to_iterate_on = str(n)[::-1]
    result = 0
    while True:
        for index, value in enumerate(n_to_iterate_on):
                result += int(value) * divisors[index]
        if str(result)[::-1] != n_to_iterate_on:
            n_to_iterate_on = str(result)[::-1]
            result = 0
        else:
            return result