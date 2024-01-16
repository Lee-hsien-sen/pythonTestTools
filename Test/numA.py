"""
#1,2,3,4 这 4 个数字，能组成多少个互不相同的且无重复的三位数，都是多少？
"""

def numA(n):
    count = 0  # 记录符合条件的三位数的数量
    # 嵌套循环生成三位数
    for i in range(1, n):
        for j in range(1, n):
            for k in range(1, n):
                if i != j and j != k and k != i:  # 确保三位数的每个位上的数字互不相同
                    num = i * 100 + j * 10 + k  # 构造三位数
                    print(num)
                    count += 1

    print("共有", count, "个互不相同且无重复的三位数")

if __name__ == '__main__':
    numA(9)