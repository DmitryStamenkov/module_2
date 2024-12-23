first = int(input('ведите целое число:'))
second = int(input('ведите целое число:'))
third = int(input('ведите целое число:'))

if first == second and second == third and first == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
else:
    print(0)
