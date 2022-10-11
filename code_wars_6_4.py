def play_pass(s, n):
    result_str, final = "", ""
    alphabet = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H", 8: "I", 9: "J",
                10: "K", 11: "L", 12: "M", 13: "N", 14: "O", 15: "P", 16: "Q", 17: "R", 18: "S", 19: "T",
                20: "U", 21: "V", 22: "W", 23: "X", 24: "Y", 25: "Z"}

    alphabet_bis = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H", 8: "I", 9: "J",
                10: "K", 11: "L", 12: "M", 13: "N", 14: "O", 15: "P", 16: "Q", 17: "R", 18: "S", 19: "T",
                20: "U", 21: "V", 22: "W", 23: "X", 24: "Y", 25: "Z"}

    for i in s:
        if i.isalpha():
            result_str += chr(ord(i)+n %26)
        elif i.isnumeric():
            result_str += str(9 -(int(i)))
        else:
            result_str += i
    for index, value in enumerate(result_str):
        if index % 2 != 0 and value.isalpha() :
            final += value.lower()
        else:
            final += value
    return final[::-1]