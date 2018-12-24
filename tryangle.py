#Triangle.py
user = input()
stars = eval(user)
row = int((stars+1)/2)
for i in range(row):
    star = '*'*((i+1)*2-1)
    lr= int((stars-((i+1)*2-1))/2)*' '
    print ('{}{}{}'.format(lr,star,lr))
