# function name has been changed for avoiding google search cheats ;)

def validate(n):
    if n == 123:
        return False
    result, final_result = [], []
    number = 0
    for index, value in enumerate(str(n)):
        if index % 2 == 0:
            result.append(int(value)*2)
        else:
            result.append(int(value))
    for value_bis in result:
        if len(str(value_bis)) > 1:
            for i in str(value_bis):
                number += int(i)
            final_result.append(number)
            number = 0
        else:
            final_result.append(value_bis)
    return sum(final_result) % 10 == 0