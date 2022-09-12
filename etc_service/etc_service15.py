from typing import List, Dict, Tuple, Set, Union, Final


def sum_list(numbers: List[int]) -> int:
    return sum(n for n in numbers)


result = sum_list([1, 2, "3", 4])
print(result)


persons: Dict[str, int] = {"홍길동": 23, "이한수": 34}
hong: Tuple[str, int, bool] = ("홍길동", 23, True)
mark: Set[str] = {"A", "B", "C", "D", "F"}


# Union : 여러 개 타입을 사용하는 경우
def add(a: int, b: Union[int, float]) -> str:
    return a + b


PORT = Final[int] = 8080
