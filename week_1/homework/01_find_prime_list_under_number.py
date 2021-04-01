input = 20


def find_prime_list_under_number(number):
    # 이 부분을 채워보세요!
    prime_list = []
    for n in range(2, number + 1):
        print(n)
        for i in prime_list:  # 2 * 3 = 6 이니까 6 은 구지 해 볼 필요가 없
            if n % i == 0 and i * i <= n:
                break
        else:
            prime_list.append(n)
    return prime_list


result = find_prime_list_under_number(input)
print(result)