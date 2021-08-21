def get_fibonacci(n):
    if n in (1, 2):
        return 1
    return get_fibonacci(n - 1) + get_fibonacci(n - 2)

print(get_fibonacci(20))