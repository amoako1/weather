def even_only(lst):
    evens = []
    for number in lst:
        if is_even(number):
            evens.append(number)
    return evens