"""
把数据存储到文件最合理的方案就是用pickle
1、dumps 把对象转化成字节
2、loads 把字节转化为对象
3、dump  把对象序列化成字节后存储到文件
4、load  把文件中的字节反序列化成对象
序列化 把对象转化为二进制字节
反序列化 把二进制字节转化为对象

模块json
json处理中文要加ensure ascii


hashlib
运用md5加密，但是md5加密已经运用了很多年，容易撞库
解决撞库的最好办法就是加盐
md5可以进行密码加密，也可以是检测文件一致性

shutil
文件操作
移动，move
复制 copyfileobj  对对象进行复制，需要使用with open
    copyfile  通过文件路径进行复制文件内容，但是不复制文件权限，修改时间
    copy  复制文件的内容和权限
    copy2 复制文件的内容和修改时间
    copystat 复制文件的修改时间和权限，但不复制内容
    copymode 只复制权限
    copytree 复制文件夹
    rmtree 删除文件夹

"""
import hashlib


def jm():  # md5加密
    obj = hashlib.md5(b'')  # fafa就是盐, 必须要用b修饰
    obj.update('旁叶易寒'.encode('utf-8'))
    print(obj.hexdigest())


def num():  # 力扣第一题 两数之和

    nums = [3, 3, 11, 15]
    target = 6
    for i in nums:
        a = target - i
        for c in range(nums.index(i) + 1, len(nums)):
            if nums[c] == a:
                return [nums.index(i), c]


def find(left, right):
    target = 2
    mid = (left + right) // 2
    print(nums[mid])
    if left <= right:
        if target == nums[mid]:
            print('找到了是', mid)
            return mid

        elif target > nums[mid]:
            left = mid+1
            find(left, right)
        elif target < nums[mid]:
            right = mid-1
            find(left, right)

    else:
        return -1
    return find(left,right)


if __name__ == '__main__':
    left = 0
    nums = [-1, 0, 3, 5, 9, 12]
    right = len(nums)
    a = find(left, right)


