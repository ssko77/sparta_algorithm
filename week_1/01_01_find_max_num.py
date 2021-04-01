input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    # 이 부분을 채워보세요!
    for num in array:
        for compare_num in array:
            if num < compare_num:
                break
        else:            # 그런데 else 의 위치가 좀 헛갈림 하여
            return num



result = find_max_num(input)
print(result)