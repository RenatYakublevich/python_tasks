# 3 решение
 
q = int(input())

t = lambda q: 5 if q == 3 else (10 if q == 5 else (15 if q == 10 else 123))
print(t(6))

