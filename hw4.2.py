def calculate_product(lst):
    if not lst:
        return 0

    even_index_sum = sum(lst[i] for i in range(0, len(lst), 2))

    last_element = lst[-1]

    result = even_index_sum * last_element

    return result

print(calculate_product([0, 1, 7, 2, 4, 8]))

print(calculate_product([1, 3, 5]))

print(calculate_product([6]))

print(calculate_product([]))
