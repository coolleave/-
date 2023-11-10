lst = list(map(int, input().split()))
lst.sort()
mid = int(len(lst) / 2)
flag = len(lst) % 2
if not flag:
    print((lst[mid-1] + lst[mid])/2)
else:
    print(lst[len(lst)//2])

