string = '1 2 3'
z = lambda s: list(map(int,s.split(' ')))
print(z(string))