import csv
import statistics 
from collections import Counter
with open('meal.csv') as csv_file:
    csv_read=csv.reader(csv_file,delimiter=",")
    line_count=0
    datas=[]
    data_f=[]
    data_1=[]
    data_2=[]
    for row in csv_read:
        if row[0]!='Meal':
            datas.append(list(row))
    print(datas)
    xi_x=[]
    yi_y=[]
    xi_x2=[]
    xi_xyi_y=[]
    for i in datas:
        del i[0]
    data_f=[[int(j) for j in i] for i in datas]
    print(data_f)
    data_1=[i[0] for i in data_f]
    x=statistics.mean(data_1)
    data_2=[i[1] for i in data_f]
    y=statistics.mean(data_2)
    for i in range(0,len(data_f)):
        xi_x.append(data_1[i] - x)
        yi_y.append(data_2[i] - y)
        xi_x2.append(xi_x[i]*xi_x[i])
        xi_xyi_y.append(xi_x[i] * yi_y[i])
    print(xi_x)
    print(yi_y)
    print(xi_x2)
    print(xi_xyi_y)
    A=sum(xi_x2)
    B=sum(xi_xyi_y)
    w1=B/A
    w0=y-w1*x
    x_val=int(input("ENTER the value of X : "))
    y_val=w0 + w1 * x_val
    print("The predicted value of Y : " + str(y_val))
