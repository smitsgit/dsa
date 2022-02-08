def merge(left, right):
    while left and right:
        if left[0] < right[0]:
            yield left.pop(0)
        else:
            yield right.pop(0)

    yield from left
    yield from right


def merge_sort(data):
    if len(data) < 2:
        return data
    mid = len(data) // 2
    return list(merge(merge_sort(data[:mid]), merge_sort(data[mid:])))


def main():
    data = [10, 40, 50, 3, 2, 70, 60, 90]
    print(merge_sort(data))


if __name__ == '__main__':
    main()
