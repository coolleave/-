def findmissnumbers():
    lst = [4,3,2,7,8,2,3,1]
    lst.sort()
    miss_lst = []
    for i in range(1, len(lst)+1):
        if i in lst:
            pass
        elif i not in lst:
            miss_lst.append(i)
    return miss_lst


if __name__ == '__main__':
    print(findmissnumbers())
