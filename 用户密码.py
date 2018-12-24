#用户密码
for i in range(3):
    user = input();
    password = input();
    if user == 'Kate' and password == '666666':
        print('登录成功！')
        break;
    else:
        if i<2:
            continue
        else:
            print('3次用户名或者密码均有误！退出程序。')
    
