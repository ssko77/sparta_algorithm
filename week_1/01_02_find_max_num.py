input = [3, 5, 6, 1, 2, 4, 7,10]


def find_max_num(array):
    # 이 부분을 채워보세요!
    max_num = array[0]
    for num in array:
        if num > max_num:
            max_num = num
    return max_num


result = find_max_num(input)
print(result)