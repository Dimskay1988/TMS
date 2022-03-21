def geometric_progression(b1: int, q: int, n: int) -> int:
    """генератор геометрической прогрессии"""
    count = 1
    while count <= n:
        yield (b1 * q ** (count - 1))
        count += 1

for num in geometric_progression(1, 2, 10):
    print(num)
