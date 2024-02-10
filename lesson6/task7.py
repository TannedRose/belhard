# дан список чисел, необходимо для каждого элемента посчитать сумму его соседей, для крайних чисел одним из соседей
#  является число с противоположной стороны
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


sum_a = []
left_ind = -1
right_ind = -len(a) + 1
ind = 0
while ind < len(a):
    print(left_ind, right_ind)
    sum_a.append(a[left_ind] + a[right_ind])
    left_ind += 1
    right_ind += 1
    ind += 1
print(sum_a)

