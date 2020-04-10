from time import time

def time_this(num_runs):
    def decorator(func):
        def wrap_func():
            time_sum = 0
            for _ in range(num_runs):
                t1 = time()
                func()
                t2 = time()
                time_sum += (t2 - t1)
            return round(time_sum / num_runs, 4)
        return wrap_func
    return decorator

@time_this(num_runs=10)
def f():
    for _ in range(1000000):
        pass
print(f"Время выполнения: {f()} секунд")