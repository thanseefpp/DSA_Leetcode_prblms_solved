import timeit

start = timeit.default_timer()
list_data = []
list_data.append(2)
list_data.append(3)
list_data.append(4)
list_data.append(5)
list_data.pop()
list_data.pop()
print(list_data)
stop = timeit.default_timer()

print('Time: ', stop - start)