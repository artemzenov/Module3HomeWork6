def calculate_structure_sum(data, sum_int_str=0):

    for elem in data:
        if isinstance(elem, int):
            sum_int_str += elem
        elif isinstance(elem, str):
            sum_int_str += len(elem)
        elif isinstance(elem, dict):
            sum_int_str = calculate_structure_sum(
                list(elem.items()),
                sum_int_str
                )
        elif isinstance(
                elem,
                (list, tuple, set, frozenset)
                ):
            sum_int_str = calculate_structure_sum(
                elem,
                sum_int_str
                )

    return sum_int_str


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
    ]

result = calculate_structure_sum(data_structure)

print(result)