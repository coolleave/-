def findKthPositive():  # 暴力遍历
    arr = [1,2]
    k = 1
    m = 0
    for i in range(1, 1000):
        if i not in arr:
            m += 1
            if m == k:
                return i


def findKthPositive1():  # 大佬的方法，二分法查找
    arr = [1, 2, 3, 4]
    k = 2
    arr.insert(0, 0)
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        temp = arr[mid] - mid
        if temp >= k:
            right = mid - 1
        else:
            left = mid + 1
    return k + right


if __name__ == '__main__':
    print(findKthPositive1())