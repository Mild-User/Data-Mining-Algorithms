  
R = int(input("Enter the number of rows:")) 
C = int(input("Enter the number of columns:")) 
  
# Initialize matrix 
matrix = [] 
print("Enter the entries rowwise:") 

outbound=[]  
# For user input 
for i in range(R):          # A for loop for row entries 
    a =[]
    outbound.append(int(input("Enter the no of outbound link")))
    for j in range(C):      # A for loop for column entries 
         a.append(int(input())) 
    matrix.append(a) 


for i in range(R): 
    for j in range(C): 
        print(matrix[i][j], end = " ") 
    print() 

d=float(input("Enter the value of d"))


list_iter=[1,1,1] # Initailising the initial list with number of 1's
print("Iteration : 0 ",list_iter)
count=[]
for m in range(0,3):       #loop for number of iterations
  for i in range(R):
    count.clear()
    for j in range(C): 
       calc=matrix[i][j]
       if(calc==1):
          count.append(j)
    sum_link=0      
    for k in count:
        sum_link=sum_link+list_iter[k]/outbound[k]
        # print("sum",sum_link)
        new_rank=(1-d) + d*(sum_link)
    list_iter[i]=new_rank
  print("Iteration : ",m+1,list_iter)
        
