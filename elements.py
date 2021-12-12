# С, КЗ,  И, ИЗ, У
def summator(input1, input2):  # Сумматор
    return input1 + input2


def usil(input, K):  # Усилитель
    return K * input


def inerz(input, T, hist):  # Инерционное
    return (input + T * hist) / (T + 1)


def integr(input, hist):  # Интегратор
    return 0.001 * input + hist


def koleb(input, T1, T2, hist1, hist2):  # Колебательное звено
    return (input + (T1 + 2 * T2) * hist1 - T2 * hist2) / (1 + T1 + T2)
