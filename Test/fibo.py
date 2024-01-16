""""
#斐波那契数列

"""


def fibonacci(n):
    fib_seq = [0, 1]  # 斐波那契数列的前两个数字

    if n <= 1:
        return fib_seq[:n + 1]  # 返回前 n+1 个数字？

    while len(fib_seq) <= n:
        next_num = fib_seq[-1] + fib_seq[-2]  # 计算下一个数字
        fib_seq.append(next_num)  # 将下一个数字添加到数列中

    return fib_seq

if __name__ == '__main__':

    # 测试生成斐波那契数列的函数
    n = 19  # 要生成的斐波那契数列的长度
    fib_nums = fibonacci(n)
    print(fib_nums)