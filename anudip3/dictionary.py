#data given by user
n=int(input("enter the value:"))
#initialize the empty list
square_dict={}

for x in range(1,n+1):
    square_dict[x]=x**2
    
#output of the program    
print("new dictionary",square_dict)    