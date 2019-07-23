import csv
from collections import Counter
import math
import random

with open('medicine.csv') as csv_file :
   csv_read = csv.reader(csv_file,delimiter =",")
   line_count=0;
   datas=[]
   data_f=[]
   n=[]
   cluster={k: [] for k in range(2)}
   k=int(input("Specify number of clusters:"))
   for row in csv_read:
        if row[0]!='Medicine':
            datas.append(list(row))
   for i in datas:
       del i[0]
   data_f=[[int(j) for j in i] for i in datas]
   print(data_f)    
   cent=cent2=[]
   k1=k
   while k!=0:
       j=random.randint(0,1)
       if data_f[j] not in cent:
           cent.append(data_f[j])
       else:
           continue
       k=k-1
   cent1=cent.copy()    
   p=0
   
   while (1):
     for j in data_f: 
           n=[]     # temporary list array for 
           for l in cent:
                eud=math.sqrt( (l[0]-j[0])**2 + (l[1]-j[1])**2 )
                n.append(eud)
           index_c=n.index(min(n))
           cluster[index_c].append(j)
           del n      
     p=p+1
     print("Mean of the clusters:")
     print(cent)
     print("Iteration  "+str(p))
     print(cluster)
     
     del cent
     cent=[]
     for i in range(0,k1):   
         temp=cluster[i]
         sum1=0
         sum2=0
         for k in temp:
            sum1=sum1+k[0]
            sum2=sum2+k[1]
         c11=sum1/len(cluster[i])
         c12=sum2/len(cluster[i])
         cent.append([c11,c12])   
     if(cent2==cent):
         break
     del cluster
     cluster={k: [] for k in range(2)}  #reinitialising the cluster
     cent2=cent.copy()

 
       
       
   
