import functools
import time


def elapsed(original_func):
    @functools.wraps(original_func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = original_func(*args, **kwargs)
        end = time.time()
        print("함수 수행 시간 : %f 초" % (end - start))
        return result

    return wrapper


@elapsed
def add(a, b):
    """
    두 수 a, b를 더한 값을 반환하는 함수
    """
    return a + b


print(add)
help(add)
