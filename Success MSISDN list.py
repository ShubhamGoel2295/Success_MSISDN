
#3rd Batch of  Job IDs for Sep-19.xlsx
import pandas as pd
import os.path
from os import path
import datetime


a= '''zgrep '8001900158703693441' /prd/im/cdrs/smsc/bkup/mts_cdr.log.20190801*|grep 'ST:1' | awk -F'|' '{ print $4 }' >/tmp/success_aug19/success_8001900158703693441.txt &''' #example data
b=a.split()

f1= open(r'Filepath', 'w')#to write O/P in a file. Giving Filepath in which u want to store the O/P.
def command_modify(sub_id, parameter_date):
    global c  # giving error i.e local variable 'c' referenced before assignment thst why made it global
    c=b
    for i, j in enumerate(b):
        if i == 1:
            temp1 = j.strip('\'')
            temp1 = c.pop(i)
            subid= '\''+ sub_id + '\''
            c.insert(i, subid)
            # print(c)

        elif i == 2:
            split_part = j.split('/')
            val = j.split('/')[6][16:20]
            temp3 = j.split('/')[6]
            split_part[6] = str(temp3).replace(val, parameter_date)
            split_part = '/'.join(split_part)
            # print(t)
            c[i] = split_part

        elif i == 11:
            k = j.split('/')
            # print(k)
            suc = [v for v in k if 'success_8' in v]
            temp2 = (''.join([i for i in str(suc) if i.isdigit()]))
            temp2= str(suc).replace(temp2, sub_id)
            k[3]=temp2.strip('[]').strip("\'")
            k='/'.join(k)
            c[i]=k
            c= ' '.join(c)
            # d=c #can assign in another one but remove global section above then
        # print(c) #we can't run outside if loop becuz see the working then get to know
        #     print(c)
            f1.write('\n'+c+'\n')# write o/p to file


filename= input('Enter the file name you want to run: ') #taking input
for roots, dirs, files in os.walk(r'C:\Users\'):  #getting input file's path
    for name in files:
        if name==filename:
            filepath= os.path.abspath(os.path.join(roots, name))


df= pd.read_excel(filepath)
pd.set_option('display.max_columns',40)
# print(df.head())
# print(df.columns.values)
cols= [list(df.columns.values).index(i) for i in df.columns.values if 'Submission' in i or 'Scheduled' in i] #taking coulmns index
# print(cols)

df1= df[df.columns[cols]]
# print(df1)

for i in df1.itertuples(): #use this to execute one row at time
    month = str(i[2])
    temp = datetime.datetime.strptime(month, '%Y-%m-%d %H:%M:%S')
    temp_day = temp.day
    temp_month = temp.month
    if len(str(temp_day)) == 1:
        temp_day = '0' + str(temp_day)
    if len(str(temp_month)) == 1:
        temp_month = '0' + str(temp_month)
    permanent_date = str(temp_month) + str(temp_day)
    # print(permanent_date)
    submission_id= str(i[1])
    command_modify(submission_id, permanent_date) #using this to modify commands
