'''
#冒泡排序
'''

def bubble_sort(arr, *args):
    n = len(arr)
    # 遍历数组元素
    for i in range(n):
        # 每次遍历将最大的元素冒泡到末尾
        for j in range(0, n - i - 1):
            # 如果当前元素大于下一个元素，则交换它们的位置
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

if __name__ == '__main__':

    # 测试冒泡排序
    arr = [64, 34, 25, 12, 22, 11, 90]
    bubble_sort(arr)

    print("排序后的数组：")
    print(arr)