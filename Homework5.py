immutable_var = 1, 'string', 2.4
print("Immutable tuple: ", immutable_var)
immutable_var = ([1, 'string'], 2.4)
print(immutable_var)
immutable_var[0] [1] = 'clone' #Значения элементов кортежа можно изменять, только если предварительно он имеет в себе изменяемые элементы
print(immutable_var)
mutable_list = [1, 'string', 2.4]
mutable_list.append("Modified")
print("Mutable list: ", mutable_list)
