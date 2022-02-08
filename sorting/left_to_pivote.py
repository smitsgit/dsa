def main():
    data = [40, 80, 90, 10, 15, 4, 70]
    last_index = len(data) - 1
    pivot = data[last_index]

    left = 0
    right = last_index - 1
    done = False

    while not done:
        while data[left] < pivot and left <= right:
            left += 1
        while data[right] > pivot and left <= right:
            right -= 1
        if left > right:
            done = True
        else:
            data[left], data[right] = data[right], data[left]

    data[left], data[last_index] = data[last_index], data[left]
    print(data)


if __name__ == '__main__':
    main()
