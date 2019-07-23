import csv
import random
import math
import string


def Apriori_prune(Ck,MinSupport):   #Ck is the dictionary
    L = []
    for i in Ck:
        if Ck[i] >= MinSupport :
            L.append(i)
    return sorted(L)

def Apriori_gen(Itemset, length):
    # forming frequent k- Itemset
    canditate = []
    canditate_index = 0
    for i in range (0,length):
        element = str(Itemset[i])
        for j in range (i+1,length):
            element1 = str(Itemset[j])
            if element[0:(len(element)-1)] == element1[0:(len(element1)-1)]:
                unionset=element[0:(len(element)-1)] + element1[len(element1)-1] + element[len(element)-1]
                unionset=''.join(sorted(unionset))
                canditate.append(unionset)
                    
    return canditate


def Apriori_count_subset(Candidate,cand_len):
    """ Use bool to know is subset or not """
    Lk = dict()
    Lk1={}
    supportData={}
    for d in datas:
        count = 0
        for i in range (0,cand_len):
            key = str(Candidate[i])
            if key not in Lk:
                Lk[key] = 0
            n=0    
            flag = True
            for k in key:
                if k not in d:
                    flag = False
            if flag:
                Lk[key] += 1
                
    #calculating support data for association rules
    """for key in Lk:
        Lk1[key]=[ [int(j) for j in i ] for i in Lk]
    print(Lk)"""
    for key in Lk:
        support=Lk[key]
        supportData[key] = support
                
   
    return Lk, supportData


with open('apriori2.csv') as csv_file :
   csv_read = csv.reader(csv_file,delimiter =",")
   line_count=0;
   datas=[]
   data_f=[]
   data_pri=[]
   tid=[]
   copy_f=[]
   count_item=C1={}
   for row in csv_read: 
       if(row[0]!='TID'):
            tid.append(row[0])
            datas.append(row[1])
   print(datas)
   datas=[i.replace(',','') for i in datas] # replacing all the commas with ""
   print(datas)
   data_f=[ [int(j) for j in i ] for i in datas] # converting each of string letter into a number
   print(data_f)
   
   # distinct value array is copy_f
   for i in data_f:
       for j in i:
           if (j not in copy_f):
              copy_f.append(j)   #print(copy_f)          
   
   #count of each of the distinct item:
   for k in copy_f:
       count=0
       ele=str(k)
       for i in datas:
           for j in i:
               if(j==ele):
                  count=count+1
       count_item[ele]=count       #print(count_item)
   #count_item.keys().sort()
   print(count_item)
   C1=count_item.copy()
   print(C1)
   
   # calculate the min_sup
   min_sup=2
   
k=2
supportData={}
for i in C1:
    supportData[i]=C1[i]
L = []
L_copy=[]
L1 = Apriori_prune(C1,min_sup)
L = Apriori_gen(L1,len(L1))  # returns a string of permuted pruned itemsets
print ('******************************************')
print ('Frequent 1-itemset is',L1)



while L != []:
    C = dict()
    C, supK = Apriori_count_subset(L,len(L))
    for i in supK:
        if i not in supportData:
           supportData[i]=supK[i]
    frequent_itemset = []
    frequent_itemset = Apriori_prune(C,min_sup)
    if frequent_itemset != []:
        print ('******************************************')
        data_pri=[ [int(j) for j in i ] for i in frequent_itemset]
        print ('Frequent',k,'-itemset is',data_pri)
        L_copy=data_pri.copy()
    L = Apriori_gen(frequent_itemset,len(frequent_itemset))
    k += 1

print()
print("Strong Association rules are : ")
rules=[]
for i in L_copy:
    cand=Apriori_gen(i,len(i))
    for j in i:
        cand.append(str(j))
    #print(cand)
    for k in cand:
        for j in cand:
            if(k!=j and len(k)!=len(j)):
                if j not in k and k not in j:
                   rules.append([k,j])

    for h in rules:
        if h[0] in h[1]:
            rules.remove(h)
    final=''
    for h in rules:
        n=[ [int(j) for j in i ] for i in h]
        final=h[0]+h[1]
        final=''.join(sorted(final))
        conf=supportData[final]/supportData[h[0]]
        if(conf>0.7):
            print(n[0],' => ' , n[1])
        



    

        
    
