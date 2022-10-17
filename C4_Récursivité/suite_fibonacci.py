import sys
import time
import matplotlib.pyplot as plt
sys.setrecursionlimit(1000000000)


def fibo(n: int) -> int:
    """Calcul de la suite de Fibonacci
    Args:
        n (int): le nombre de la suite de Fibonacci
    Returns:
        int: le nombre de la suite de Fibonacci
    """
    if n > 1:
        return fibo(n - 1) + fibo(n - 2)
    return n


def fibo_memo(n: int) -> int:
    """Calcul de la suite de Fibonacci avec mémorisation
    Args:
        n (int): le nombre de la suite de Fibonacci
    Returns:
        int: le nombre de la suite de Fibonacci
    """
    memo = {0: 0, 1: 1}

    def fibo(n) -> int:
        if n not in memo:
            memo[n] = fibo(n - 1) + fibo(n - 2)
        return memo[n]

    return fibo(n)


def fibo_itteration(n: int) -> int:
    """Calcul de la suite de Fibonacci avec itération
    Args:
        n (int): le nombre de la suite de Fibonacci
    Returns:
        int: le nombre de la suite de Fibonacci
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for i in range(2, n + 1):
            a, b = b, a + b
        return b

def graphique(fibonacci, n: int) -> float:
    times = []
    fiboX = []

    for i in range(n):
        depart = time.perf_counter()
        x = fibonacci(i)
        fin = time.perf_counter()
        currenttime = fin - depart
        times += [currenttime]
        fiboX += [i]
    plt.plot(fiboX, times)
    plt.show()
    return f"Temps d'exécution: {fin - depart} secondes de fibo"

if __name__ == "__main__":
    print(graphique(fibo, 20))
    print(graphique(fibo_memo, 2000))
    print(graphique(fibo_itteration, 2000))
