import numpy as np
a = np.array([1,2,3])
b = np.array([[1,2,3],[4,5,6],[7,8,9]])
b[1,1] = 10
print(a.shape)
print(b.shape)
print(a.dtype)
print(b)

""" Practice for struct array """
persontype = np.dtype({
    'names':['name', 'age', 'chinese', 'math', 'english'],
    'formats':['S32', 'i', 'i', 'i', 'f']})

peoples = np.array([("ZhangSan", 32, 75, 100, 90),
("LiSi", 24, 85, 96, 88.5),("MaZi", 29, 65, 85, 100)],
dtype = persontype)
names = peoples[:]['name']
ages = peoples[:]['age']
chineses = peoples[:]['chinese']
print(names)
print(ages)
print(chineses)
print(np.mean(chineses))

""" 创建连续数组 """
x1 = np.arange(1,11,2)
x2 = np.linspace(1,9,5)
print('x1: {0}'.format(x1))
print('x2: {0}'.format(x2))
""" 算术运算 """
print(np.add(x1, x2))
print(np.subtract(x1, x2))
print(np.multiply(x1, x2))
print(np.divide(x1, x2))
print(np.power(x1, x2))
print(np.remainder(x1, x2))
print(np.mod(x1, x2))

""" 计数组 / 矩阵中的最大值函数 amax()，最小值函数 amin() """
a = np.array([[1, 2, 3],[4, 5, 6],[7, 8 ,9]])
print(np.amin(a))
print(np.amin(a,0))
print(np.amin(a,1))

""" 统计最大值与最小值之差 """
print(np.ptp(a))
print(np.ptp(a, 0))
print(np.ptp(a, 1))

""" 统计数组的百分位数 """
print(np.percentile(a,50))
print(np.percentile(a, 100,axis=0))
print(np.percentile(a, 0, axis=1))


""" Find the median number """
print(np.median(a))
print(np.median(a, axis=0))
print(np.median(a, axis=1))

""" Find the mean """
print(np.mean(a))
print(np.mean(a, axis=0))
print(np.mean(a, axis=1))

""" Calculate the average of the numbers of a array """
a2 = np.array([1, 2, 3, 4])
wts = np.array([1, 2, 3, 4])
print(np.average(a2))
print(np.average(a2, weights=wts))

""" 统计数组中的标准差 方差 """
print(np.std(a2))
print(np.var(a2))

""" Rank """
a3 = np.array([[4, 3, 2],[2, 4, 1]])
print(np.sort(a3))
print(np.sort(a3, axis=None))
print(np.sort(a3, axis=0))
print(np.sort(a3, axis=1))