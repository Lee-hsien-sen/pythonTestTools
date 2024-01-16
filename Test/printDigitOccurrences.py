"""
#给定一个整数 N，和一个 0-9 的数K，要求返回0-N中数字K出现的次数
#
"""
def print_digit_occurrences(N, K):
    my_dic = {}
    for num in range(N + 1):
        digits = list(str(num))
        occurrences = digits.count(str(K))
        if occurrences > 0:
            my_dic[num] = occurrences
            print(f"数字 {K} 在 {num} 中出现了 {occurrences} 次")
    print("数组出现的数据:", my_dic)

if __name__ == "__main__":
    N = 100
    K = 2



    print_digit_occurrences(N, K)

