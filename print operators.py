n=int(input("enter :"))
a=input("Enter :").split()
x,y=map(int,input("enter :").split())
for i in a:
    if(x//y==int(i)):print('/',end=" ")
    elif(x*y==int(i)):print('*',end=" ")
    elif(x+y==int(i)):print('+',end=" ")
    elif(x-y==int(i)):print('-',end=" ")
    else:print('#',end=" ")
