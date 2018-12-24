#The Progress bar
#Bar 1
import time 
scale=50
print('{:-^20}'.format('执行开始'))
start = time.perf_counter()
for i in range(scale+1):
    star = '*'*i
    line = '-'*(scale-i)
    rate = i*2
    end = time.perf_counter()-start
    print('\r{}%[{}->{}]{:.2f}s'.format(rate,star,line,end))
    time.sleep(0.1)
print('{:-^20}'.format('执行开始'))
