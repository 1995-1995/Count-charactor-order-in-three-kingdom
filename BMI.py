#BMI
height, weight = eval(input())
BMI = weight/(height**2)
if (BMI)<18.5:
    nat ='偏瘦'
    intnat='偏瘦'
elif 18.5 <= BMI <24:
    nat ='正常'
    intnat='正常'
elif 24 <= BMI <25 :
    nat ='偏胖'
    intnat='正常'
elif 25<= BMI < 28:
    nat ='偏胖'
    intnat='偏胖'
elif 28<= BMI < 30:
    nat ='肥胖'
    intnat='偏胖'
else:
    nat ='肥胖'
    intnat='肥胖'
print('BMI 数值为: {:.2f}'.format(BMI))
print('BMI 指标为: 国际{}, 国内{}'.format(nat,intnat))
