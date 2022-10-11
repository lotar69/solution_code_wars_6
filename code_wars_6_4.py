# function name has been changed for avoiding google search cheats ;)

def changed(s, n):
    result_str, final = "", ""
    for i in s:
        if i.isalpha():
            result_str += chr((ord(i) - 65 + n % 26) % 26 + 97)
        elif i.isnumeric():
            result_str += str(9 -(int(i)))
        else:
            result_str += i
    for index, value in enumerate(result_str):
        if index % 2 == 0 and value.isalpha():
            final += value.upper()
        else:
            final += value
    return final[::-1]