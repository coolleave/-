def dele():  # 列表去重
    nums = [1, 1, 2]
    nums = list(set(nums))
    print(nums)
    return len(nums)


def find():  # 搜索插入位置
    nums = [1, 3, 5, 6]
    target = 7
    if target in nums:
        return nums.index(target)
    else:
        nums.append(target)
        nums.sort()
    return nums, nums.index(target)


def combine1():  # 合并数列 方法1自己的方法
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    if nums1:
        nums1 = nums1[:m]
    if nums2:
        nums2 = nums2[:n]
    nums1 = nums1 + nums2
    nums1.sort()
    return nums1


def combine2():  # 方法2，逃课方法
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    nums1[m:] = nums2[:]


def combine3():  # 方法三 双指针倒序法
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    # 因为叫倒序法，所以查找和添加元素都是从后边开始，也就是从大到小
    # l 为nums1的索引 从大到小，r为nums2的索引 从大到小
    # index为合并后列表的索引 从大到小
    l, r, index = m - 1, n - 1, len(nums1) - 1
    # 指针1就是 nums1[l]
    # 指针2就是 nums2[r]
    # 两个指针比较大小，大的就写入num1[index],然后相应的索引-1
    while l >= 0 and r >= 0:
        if nums1[l] > nums2[r]:  # 指针1大，写入指针1
            nums1[index] = nums1[l]
            l -= 1
        elif nums1[l] < nums2[r]:  # 指针2大，写入指针2
            nums1[index] = nums2[r]
            r -= 1
        elif nums1[l] == nums2[r]:  # 两个指针相等，分别写入
            nums1[index] = nums2[r]
            index -= 1
            r -= 1
            nums1[index] = nums1[l]
            l -= 1
        index -= 1  # 本次指针写入后，索引-1
    while r >= 0:  # 当nums1索引完，但nums2还有时（r>=0,l<0），就把nums2的索引再写入，直到全部完成
        nums1[index] = nums2[r]
        r -= 1
        index -= 1
    # 当nums1索引剩余时(l>=0,r<0)怎么办呢，因为我们本身就是往nums写的，所以就算剩下，也就在nums1中不用写
    return nums1


if __name__ == '__main__':
    print(combine3())
