# function name has been changed for avoiding google search cheats ;)

def changed(array, runs):
    new_array = []
    counter = 0
    if len(array) % 2 == 0:
        while counter < runs:
            half_of_even_array = len(array)//2
            first_part, second_part = array[:half_of_even_array], array[half_of_even_array:][::-1]
            for i in range(0, half_of_even_array):
                new_array.append(first_part[i] + second_part[i])
                counter += 1
            array = new_array
            new_array = []
            counter += 1
        return array
    while counter < runs:
        half_of_odd_array_without_middle = len(array)//2
        middle = len(array)//2
        first_part, middle_solo, second_part = array[:half_of_odd_array_without_middle], array[middle], array[half_of_odd_array_without_middle+1:][::-1]
        for i in range(0, half_of_odd_array_without_middle):
            new_array.append(first_part[i] + second_part[i])
        new_array.append(middle_solo)
        counter += 1
        if counter == runs:
            return new_array
        array = new_array
        new_array = []
        if len(array) == 2:
            return [sum(array)]


print(fold_array([74, 76, 81, 92, 104], 1))
#9 6

# [1, 2, 3, 4, 5], 2
#9 6

# [-9, 9, -8, 8, 66, 23] 1
# [14, 75, 0]

