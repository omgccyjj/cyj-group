# 冒泡排序算法实现

def bubble_sort(arr):
    """实现冒泡排序算法
    
    参数:
        arr: 待排序的列表
    
    返回:
        排序后的列表
    """
    n = len(arr)
    # 遍历所有数组元素
    for i in range(n):
        # 标记本次循环是否发生交换
        swapped = False
        # 每次遍历后，最大元素会"冒泡"到末尾
        # 所以每次循环的范围可以缩小
        for j in range(0, n - i - 1):
            # 比较相邻元素，如果前面的大于后面的则交换
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # 如果本次循环没有发生交换，说明数组已经有序，可以提前结束
        if not swapped:
            break
    return arr

# 测试代码
if __name__ == "__main__":
    # 测试用例
    test_arr = [64, 34, 25, 12, 22, 11, 90]
    print("原始数组:", test_arr)
    sorted_arr = bubble_sort(test_arr)
    print("排序后数组:", sorted_arr)
    
    # 额外测试用例：已排序数组
    test_arr2 = [1, 2, 3, 4, 5]
    print("\n原始数组(已排序):", test_arr2)
    sorted_arr2 = bubble_sort(test_arr2)
    print("排序后数组:", sorted_arr2)
    
    # 额外测试用例：逆序数组
    test_arr3 = [5, 4, 3, 2, 1]
    print("\n原始数组(逆序):", test_arr3)
    sorted_arr3 = bubble_sort(test_arr3)
    print("排序后数组:", sorted_arr3)