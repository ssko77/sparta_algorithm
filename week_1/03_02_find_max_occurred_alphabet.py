input = "hello my name is sparta"

def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord("a")
        alphabet_occurrence_array[arr_index] += 1
    return alphabet_occurrence_array

    return max_alphabet


max_alphabet = find_max_occurred_alphabet(input)
print(max_alphabet)