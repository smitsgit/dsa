def selection_sort():
    data = [10, 40, 50, 3, 2, 70, 60, 90]
    last_index = len(data) - 1

    for index in range(last_index):
        position_of_least = index
        for i in range(index + 1, last_index + 1):
            if data[i] < data[position_of_least]:
                position_of_least = i

        if position_of_least != index:
            data[position_of_least], data[index] = data[index], data[position_of_least]

    print(data)


if __name__ == '__main__':
    # main()
    selection_sort()
