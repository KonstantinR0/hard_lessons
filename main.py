def maximum_iz_2(a, b):
    return max(a, b)
result = max(5, 34)

print(result)

def emptiness():
    pass

print("Функция определена, но пока ничего не делает.")

def maximum_iz(a, b):
    return max(a, b)
def test_max():
    assert max(40, 2), "Ошибка: максимум(40, 2) должен быть равен 40"
    assert max(-1, 1), "Ошибка: максимум(-1, 1) должен быть равен 1"
    assert max(0, 0) == 0, "Ошибка:  максимум(0, 0) должен быть равен 0"
test_max()
print("Все тесты пройдены!")


def generator(n):
    yield 1
    yield 2
    yield 3
for result = (n % 2) == 0  in generator():
    print(result)