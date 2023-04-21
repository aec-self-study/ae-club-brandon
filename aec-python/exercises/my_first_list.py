my_first_list = ['apple', 1, 'banana', 2]

cal_lookup = {'apple': 95, 'banana': 105, 'orange': 45}

for i in my_first_list:
    if isinstance(i, int):
        print(i**2)
    elif i in cal_lookup:
        print(cal_lookup[i])
    else:
        print("We don't know what to do here")