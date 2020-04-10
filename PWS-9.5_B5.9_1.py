from time import time

class Timer:
    def __init__(self, num_runs):
        self.num_runs = num_runs

    def __call__(self, func):
        def wrap_func():
            time_sum = 0
            for _ in range(self.num_runs):
                t1 = time()
                func()
                t2 = time()
                time_sum += (t2 - t1)
            return round(time_sum / self.num_runs, 4)
        return wrap_func

@Timer(num_runs=10)
def f():
    for _ in range(1_000_000):
        pass
print(f"Время выполнения: {f()} секунд")
