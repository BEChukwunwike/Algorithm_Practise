def linear_search(list, target):
    """
    :param list:
    :param target:
    :return: the index position of the target if found, else returns None
    """

    for i in range(0, len(list)-1):
        if list[i] == target:
            return i
    return None


def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not in list")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = linear_search(numbers, 9)

verify(result)