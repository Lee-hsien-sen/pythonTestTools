"""
#检查是对称数
"""
def is_symmetric_number(num):
    # 将数字转换为字符串
    num_str = str(num)

    # 检查数字的左右对称性
    if num_str == num_str[::-1]:
        return True
    else:
        return False


if __name__ == '__main__':

    # 打印 10000 以内的对称数
    for i in range(1, 10001):
        if is_symmetric_number(i):
            print(i)