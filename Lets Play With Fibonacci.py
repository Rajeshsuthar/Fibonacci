def fibonacci_series(limit):
    fib_series = []
    a, b = 0, 1
    while a <= limit:
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

limit = 50
fib_series = fibonacci_series(limit)
print("Fibonacci series between 0 and", limit, ":", " ".join(map(str, fib_series)))
