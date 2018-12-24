from turtle import *
import time as t
setup(500,300,200,200)
penup()
bk(100)
pd()
pensize(15)
color('purple')
for i in range(10):
    fd(20)
    print('\r{:.2%}'.format((i+1)*0.1))
    t.sleep(0.2)
    
    
    

    
    
    
