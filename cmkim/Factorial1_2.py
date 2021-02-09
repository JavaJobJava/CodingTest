def factorial_recursive(n):
    if (n==1) : return 1

    return factorial_recursive(n-1)*n

print(factorial_recursive(5))