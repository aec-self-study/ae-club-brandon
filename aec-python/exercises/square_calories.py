def square_calories(dictionary):
    [print(v**2) for v in dictionary.values()]

cal_lookup = {'apple': 95, 'banana': 105, 'orange': 45}

square_calories(cal_lookup)
