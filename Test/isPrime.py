""""
#素数
"""
from math import sqrt


def is_prime(num):
    # 排除小于 2 的数
    if num < 2:
        return False

    # 检查 num 是否能被 2 到 sqrt(num) 之间的整数整除
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True

if __name__ == '__main__':

    # 判断 101 到 200 之间的素数并输出
    count = 0  # 记录素数的数量

    for num in range(101, 201):
        if is_prime(num):
            print(num)
            count += 1

    print("101 到 200 之间共有", count, "个素数")