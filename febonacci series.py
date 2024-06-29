def fibonacci(n):
    fib_series = [0, 1]

    if n <= 0:
        return "Please enter a positive integer for the number of elements in the series."
    elif n == 1:
        return [0]
    elif n == 2:
        return fib_series

    while len(fib_series) < n:
        next_num = fib_series[-1] + fib_series[-2]
        fib_series.append(next_num)

    return fib_series
n = 12
fib_series = fibonacci(n)
print(fib_series)