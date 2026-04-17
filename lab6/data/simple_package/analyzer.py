def calculate_mean(num_list):
    sum = 0
    for i in range(len(num_list)):
        sum += num_list[i]
    return sum/(len(num_list))

def find_max(num_list):
    max = -100000
    for i in range(len(num_list)):
        if(num_list[i] >= max):
            max = num_list[i]
    return max

def find_min(num_list):
    min = 100000
    for i in range(len(num_list)):
        if(num_list[i] <= min):
            min = num_list[i]
    return min