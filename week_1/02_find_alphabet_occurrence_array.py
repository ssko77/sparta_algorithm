print(ord('a'))
print(ord('c') - ord('a'))

# alphabet_occurrence_array = [0] * 26
# print(alphabet_occurrence_array)

print("a".isalpha())    # True
print("1".isalpha())    # False

def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    for char in string :
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord("a")
        alphabet_occurrence_array[arr_index] += 1
    max_occurrence = 0
    max_alphabet_index = 1
    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]

        if alphabet_occurrence > max_occurrence:
            max_alphabet_index = index
            max_occurrence = alphabet_occurrence
    print(max_alphabet_index)
    return chr(max_alphabet_index + ord("a"))


    # 이 부분을 채워보세요!



print(find_alphabet_occurrence_array("hello my name is sparta"))