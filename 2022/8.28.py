import threading
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
def fn(argus):
    for a in range(100):
        print('func', argus)
# if __name__ == '__main__':  # 意思是在本py文件中执行的代码 作为模块被导入时不执行
    # t = threading.Thread(target=func)  # 创建线程并且给线程安排一个任务
    # t.start()  # 只是开始 具体时间由cpu决定
    # for i in range(100):
    #     print('main', i)

# 利用线程池进行
if __name__ == '__main__':
    with ThreadPoolExecutor(50) as t:
        for i in range(100):
            t.submit(fn, argus=f'线程{i}')
