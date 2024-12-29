import random
n = random.randint(3, 20)
print(n, '- число из первой вставки.')

list_ = []
for i in range(1, 20):
    for j in range(1, 20):
        if i < j and n % (i + j) == 0:
            list_.extend([i, j])

result = ''
for i in list_:
    result += str(i)

print(result, '- нужный пароль.')
