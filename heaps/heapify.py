def heapify(lst, index):
    left_child_index = 2 * index + 1
    right_child_index = 2 * index + 2
    largest_index = index
    if left_child_index < len(lst) and lst[left_child_index] > lst[largest_index]:
        largest_index = left_child_index
    if right_child_index < len(lst) and lst[right_child_index] > lst[largest_index]:
        largest_index = right_child_index

    if largest_index != index:
        lst[largest_index], lst[index] = lst[index], lst[largest_index]
        # This is to adjust when you reach the root and it ends up affecting, its left
        # or right subtree
        # https: // www.youtube.com / watch?v = Q_eia3jC9Ts 36:05s
        heapify(lst, largest_index)


def insert(lst: list, value):
    lst.append(value)
    heapify(lst, len(lst) - 1)


def remove(lst: list):
    item = lst[0]
    print(f"removing {item}")
    # copy the last element to first
    lst[0] = lst[len(lst) - 1]
    # reduce the size of the list
    lst.pop()
    # start heapifying at the start and only adjust the affected subtree
    heapify(lst, 0)
    return item


def main():
    data = [20, 30, 10, 40, 5, 70]
    non_leaf_node_index = len(data) // 2 - 1
    for root_index in range(non_leaf_node_index, -1, -1):
        heapify(data, root_index)

    print(data)
    remove(data)
    print(data)


if __name__ == '__main__':
    main()
