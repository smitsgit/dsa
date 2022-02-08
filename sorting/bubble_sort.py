def bubble_sort():
    data = [10, 40, 50, 3, 2, 70, 60, 90]
    last_index = len(data) - 1
    for index in range(last_index, 0, -1):
        swapped = False
        for i in range(index):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                swapped = True
        if not swapped:
            break

    print(data)


if __name__ == '__main__':
    # main()
    bubble_sort()
