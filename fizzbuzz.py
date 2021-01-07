q = int(input())

t = lambda q: 'Fizz' if q % 3 == 0 else ('Buzz' if q % 5 == 0 else ('FizzBuzz' if q % 3 == 0 and i % 5 == 0 else q))
print([t(q) for q in range(1,101)])

