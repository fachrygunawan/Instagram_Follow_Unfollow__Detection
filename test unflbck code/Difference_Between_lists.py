def print_difference_between_lists(list1, list2):
    set1 = set(list1)
    set2 = set(list2)

    only_in_list1 = set1 - set2
    only_in_list2 = set2 - set1

    return only_in_list1, only_in_list2