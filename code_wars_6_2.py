# function name has been changed for avoiding google search cheats ;)

def changed(array, runs):
    new_array = []
    counter = 0
    while counter < runs:
        if len(array) % 2 == 0:
            half_of_even_array = len(array)//2
            first_part, second_part = array[:half_of_even_array], array[half_of_even_array:][::-1]
            for i in range(0, half_of_even_array):
                new_array.append(first_part[i] + second_part[i])
            array = new_array
            new_array = []
            counter += 1
        else:
            half_of_odd_array_without_middle = len(array)//2
            middle = len(array)//2
            first_part, middle_solo, second_part = array[:half_of_odd_array_without_middle], array[middle], array[half_of_odd_array_without_middle+1:][::-1]
            for i in range(0, half_of_odd_array_without_middle):
                new_array.append(first_part[i] + second_part[i])
            new_array.append(middle_solo)
            array = new_array
            new_array = []
            counter += 1
    return array

