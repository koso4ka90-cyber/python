"""
0405_range_и_итерации
"""

count = 0 
while count < 10:
    print(count)
    count += 1

print()

""" 
start - начальный индекс
stop - конечный индекс, stop - не включается
step - шаг
"""

# range(stop)
# range(start, stop)
# range(start, stop, step)
    
for i in range(10):
    print(i)

print()

for i in range(3, 10):
    print(i)
    
print()

for i in range(3, 10, 2):
    print(i)
    
print(range(5999999999999999))
# for i in range(5999999999999999):
#     print(i)

r = range(10, 0, -1)
print(list(r))
# e, i, j, k

    
for i in range(2):
    for j in range(2):
        for k in range(2):
            print(i, j, k)
            
print('e' in 'hello')
print(123456789 in range(1000000000))
