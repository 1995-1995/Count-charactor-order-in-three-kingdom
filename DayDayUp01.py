#DayDayUp01.py
def dayUp(df):
    Capacity = 1
    for i in range(365):
        if (i%7 == 6):
            Capacity = Capacity*(1-df/2)
        else:
            Capacity = Capacity*(1+df)
    print ('After 365 day your capacity is: {:.2f}'.format(Capacity))
dayUp(0.001)
Weight = 160*0.86
print('{:.2f}'.format(Weight))

            
    
