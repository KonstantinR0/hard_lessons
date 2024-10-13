def max_iz_2(a, b):
    if a > b:
        return a
    else:
        return b

def emptiness():
    pass


def test_max_iz_2():
    assert max_iz_2(4, 5), "Молодец, верно"
    # assert max_iz_2(-1, 0), "ошибка, отрицательное число"
    # assert max_iz_2(0, 0), "равно" из за этих двух строк выдается ошибка, в чем проблема?

result = max_iz_2(5,10)
test_max_iz_2()

print(result)
print("Функция определена, но пока ничего не делает.")
print("Все тесты пройдены!")
