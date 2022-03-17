def GeneratorG_P(b1: int, q: int, n: int) -> int:
    """Генератор геометрической прогрессии"""
    count = 1
    while count <= n:
        yield (b1 * q ** (count - 1))
        count += 1

for num in GeneratorG_P(1, 2, 10):
    print(num)
