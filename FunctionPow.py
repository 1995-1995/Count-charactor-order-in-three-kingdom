#FunctionPow
value = input()
value2 = pow(eval(value),3)
if len(str(value2)) < 20:
    print('{:-^20}'.format(value2))
else:
    print(value2)
