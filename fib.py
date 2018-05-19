def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)



def main():
    num = 5
    print("I am going to calculate the fibonacci series")
    print(fib(num))
