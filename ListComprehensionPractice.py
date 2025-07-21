def find_symmetric_difference(set1, set2):
    return set1.symmetric_difference(set2)
set_a1 = {'blue', 'green'}
set_a2 = {'blue', 'yellow'}
result_a = find_symmetric_difference(set_a1, set_a2)
print("A. Symmetric difference:", result_a)
set_b1 = {1, 2, 3, 4, 5}
set_b2 = {1, 5, 6, 7, 8, 9}
result_b = find_symmetric_difference(set_b1, set_b2)
print("B. Symmetric difference:", result_b)