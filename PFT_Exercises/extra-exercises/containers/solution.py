def add_to_list(the_list, value):
    """Add value to the end of the_list, if it is not already
    in the list"""
    if not value in the_list:
        the_list.append(value)
    return the_list


def remove_non_integers(the_dict):
    """Remove all entries from the_dict whose
    values cannot be converted to integers.
    Hint: int(value) will attempt to convert value to an int"""
    for key in list(the_dict.keys()):
        try:
            int(the_dict[key])
        except ValueError:
            del the_dict[key]

    return the_dict


def all_in_set(the_set, the_list):
    """Return True if all values of the_list are also in the_set"""
    for item in the_list:
        if not item in the_set:
            return False
    return True
