"""Дан массив чисел, состоящий из некоторого количества подряд идущих единиц,
   за которыми следует какое-то количество подряд идущих нулей: 111111111111111111111111100000000.
   Найти индекс первого нуля (то есть найти такое место, где заканчиваются единицы, и начинаются нули)

"""


def task_string(string):
    index = string.find('10')
    return index + 1


def task_array(array):
    i = 0
    j = len(array) - 1
    k = (j - i) // 2  # средний элемент массива
    while i <= j:
        """Итеративный бинарный поиск.
        Каждую итерацию цикла "отбрасываем" половину массива
        """
        if array[k] == 1:
            i += k
            if array[k] == 0:
                return k
            if array[k + 1] == 0:
                return k + 1
        else:
            j -= k
            if array[k] == 1:
                return k
            if array[k - 1] == 1:
                return k - 1
        k = i + (j - i) // 2


print(task_string('111111111111111111111111100000000'))
print(task_array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]))
