def contains_double_digit(n):
    n_str = str(n)
    return any((n_str.count(x) == 2 for x in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]))

def never_decreases(n):
    n_list = [int(x) for x in str(n)]
    return sorted(n_list) == n_list

def meets_criteria(n):
    return contains_double_digit(n) and never_decreases(n)

# 147981-691423
print(len([x for x in range(147981, 691423) if meets_criteria(x)]))

