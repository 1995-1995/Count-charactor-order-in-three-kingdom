#蒙特卡罗y圆
from random import *
from time import perf_counter
dot = 1000000
circle = 0
sq = 0
start = perf_counter()
for i in range (dot):
    x,y = random(),random()
    distance = x**2+y**2
    if distance <= 1:
        circle += 1
area = circle/dot
pi = area*4
end = perf_counter()-start
print('pi equals to: {}'.format(pi))
print('it takes {}s to finish calculating'.format(end))
