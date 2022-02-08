def partition_easy(data, start_index, end_index):
    pivot = data[end_index]
    left = start_index
    right = end_index - 1
    done = False

    while not done:
        while left <= right and data[left] < pivot:
            left += 1
        while left <= right and data[right] > pivot:
            right -= 1

        if left > right:
            done = True
        else:
            data[left], data[right] = data[right], data[left]

    data[left], data[end_index] = data[end_index], data[left]
    return left


def partition(data, start_index, end_index):
    pivot = data[end_index]
    p_index = start_index

    for i in range(start_index, end_index):
        if data[i] < pivot:
            data[i], data[p_index] = data[p_index], data[i]
            p_index += 1

    data[p_index], data[end_index] = data[end_index], data[p_index]
    return p_index


def quick_sort(data, start_index, end_index):
    if start_index < end_index:
        # p_index = partition(data, start_index, end_index)
        p_index = partition_easy(data, start_index, end_index)
        quick_sort(data, start_index, p_index - 1)
        quick_sort(data, p_index + 1, end_index)


if __name__ == '__main__':
    data = [70, 30, 40, 10, 50]
    quick_sort(data, 0, len(data) - 1)
    print(data)
