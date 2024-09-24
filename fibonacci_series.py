print("....FIBONACCI SERIES....")
num = int(input("enter the length of seires: "))

def fibonacci(num):
    fibo_list = []
    for i in range(0,num+1):

        if(i<2):
            fibo_list.insert(i,i)
        else:
            fibo_var = fibo_list[i-1] + fibo_list[i-2]
            fibo_list.insert(i,fibo_var)
    
    return fibo_list

print(fibonacci(num))