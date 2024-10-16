def max_iz_2(a, b):
    if a > b:
        return a
    else:
        return b

def emptiness():
    pass

def name(n):
    for i in range(0, n + 1, 2):
        yield i

def test_max_iz_2():
    assert max_iz_2(4, 5), "Молодец, верно"
    assert max_iz_2(-1, 0), "ошибка, отрицательное число"
    assert max_iz_2(0, 0), "равно"
    return a > b

result = max_iz_2(5, 10)
result2 = list(name(100))

print(result)
print("Функция определена, но пока ничего не делает.")
print(result2)
print("Все тесты пройдены!")
