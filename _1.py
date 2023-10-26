# '''num=[]
# for i in range(1,101):
#     if i %2 == 0:
#         num.append(i)
# print(num)
# print(len(num))'''
#
#
# '''for i in range(1,10):
#     for j in range(1,10):
#         if j <= i :
#             print(f'{j}*{i}={j*i}\t',end="")
#     print()
# '''
#
# '''import random
# money=4000
# salary_index=[]
# i=1
# while i <= 10:
#     num = random.randint(1, 10)
#     salary_index.append(num)
#     i+=1
# print(salary_index)
# k=0
# for a in salary_index:
#     k+=1
#     if a >= 5:
#         if money <= 0:
#             print('工资已发放完毕')
#             break
#         else:
#             money -= 1000
#             print(f'给第{k}人发工资后资金还剩{money}元')
#             continue
#     else:
#         print(f'第{k}员工分数过低不满足领取工资条件')
#         continue
# '''
#
# '''def temperature(x):
#     if x <= 37.5:
#         print(f'您的体温是{x}，允许进入')
#     else:
#         print(f'您的体温是{x}，体温过高不允许进入 ')
# temperature(float(input('请输入你的体温')))
# '''
#
# # money =float(5000000)
# # name = input('请输入你的名字')
# # print('''----------主菜单----------
# #          查询余额  【输入1】
# #          存款     【输入2】
# #          取款     【输入3】)
# #          退出     【输入4】''')
# # while True:
# #     choice = input('请输入选项')
# #     if choice == '1':
# #         print(f'''----------查询余额----------
# #               {name},您好，您的余额剩余：{money}元''')
# #         continue
# #     if choice == '2':
# #         deposit=float(input('请输入你的存款金额'))
# #         money += deposit
# #         print(f'''----------存款----------
# #         {name}，您好，您存款{deposit}元成功)
# #         {name}，您好，您的余额剩余{money+deposit}元''')
# #         continue
# #     if choice == '3':
# #         withdraw=float(input('请输入你的取款金额'))
# #         money -= withdraw
# #         print(f'''----------取款----------
# #         {name}，您好，您取款{withdraw}元成功)
# #         {name}，您好，您的余额剩余{money-withdraw}元''')
# #         continue
# #     else:
# #         break

first_names = ['Dwayne', 'Ryan', 'Mark', 'Ben', 'Vin']
middle_names = ['"The Rock"', 'Rodney', 'Robert Michael', 'Geza',""]
last_names = ['Johnson', 'Reynolds', 'Wahlberg', 'Affleck', 'Diesel']
f=0
while f <= 4:
    m=0
    while m <= 4:
        if middle_names[m] != None:
            l=0
            while l <= 4:
                print(f'{first_names[f]} {middle_names[m]} {last_names[l]}')
                l += 1
        else:
            l=0
            while l <= 4:
                print(f'{first_names[f]} {last_names[l]}')
                l += 1
        m += 1
    f += 1
#
# for i in first_names:
#     for j in middle_names:
#         for k in last_names:
#             if j=="":
#                 a=i+" "+k
#             else:
#                 a=i+" "+j+" "+k
#             print(a)
