input = "abadabac"


def find_not_repeating_first_character(string):
    # 이 부분을 채워보세요!
    alphabet_occurrence_array = [0] * 26

    for char in string :
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord("a")
        alphabet_occurrence_array[arr_index] += 1

    not_repeating_character_array = []

    for index in range (len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]
        if alphabet_occurrence == 1:
            not_repeating_character_array.append(chr(index + ord("a")))

    print(not_repeating_character_array)

    for char in string:
        if char in not_repeating_character_array:
            print(char)
            return char

    return "_"


result = find_not_repeating_first_character(input)
print(result)