tkts=[1,2,3,4,5,]
print('avilabe tkts',tkts)
user_input=int(input('enter how many tkts u wanna buy'))
for x in range(user_input):
     tickt_num=int(input('enter tckt number'))
     tkts.remove(tkts.num)
print('avilabe tkts', tkts)

lst=[1,2,3,4,1,2]
#op:[1,2,3,4]
emp_1st=[]
for x in lst:
    if x not in emp_1st:
        emp_1st.append(x)
print(emp_1st)


