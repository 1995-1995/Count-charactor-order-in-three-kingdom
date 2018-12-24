#水仙花数.py
Str = '';
for i in range(100,1000):
    one = eval(str(i)[0]);
    two = eval(str(i)[1]);
    three = eval(str(i)[2]);
    Sum = one**3+two**3+three**3;
    if Sum == i:
        if (i<999):
            Str += str(i)+','
print(Str[0:-1])
    
