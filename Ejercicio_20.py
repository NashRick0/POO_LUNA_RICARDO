conjunto1 = {4, 6, 9, 0, 2}
print(conjunto1)
conjunto2 = {1, 5, 1, 7, 9}
print(conjunto2)
conjunto3 = {4, 0, 4, 5, 8}
print(conjunto3)

union = conjunto1 | conjunto2 | conjunto3
conjunto1.union(conjunto2, conjunto3)
print(union)

for i in union:
    if i %2 == 0:
        new_con = i
        print(new_con)