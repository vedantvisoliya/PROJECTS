# creating a function which can find the minimum number in the list
numbers = [560,450,456,767,345,150,987,634,589,238,189,899]

def minimum_num(num_list):
    mini_num = 0
    num_list_length = len(num_list)
    for nums in range(0,num_list_length):
        if(nums == 0):
            mini_num = num_list[nums]
        elif(mini_num > num_list[nums]):
            mini_num = num_list[nums]
        
        if(nums == (num_list_length-1)):
            return mini_num


print(minimum_num(numbers))
