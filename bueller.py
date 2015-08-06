def sort_by_last_name(names):
    # create a list for the result
    result = []

    # loop through the names, modifying each and adding it
    # to the result array
    for name in names:
        first_and_last = name.split(" ")
        last_and_first = reversed(first_and_last)
        name = ", ".join(last_and_first)
        result.append(name)

    # Sort alphabetically - last name is now at front of string
    result.sort()

    # Return the result list
    return result
