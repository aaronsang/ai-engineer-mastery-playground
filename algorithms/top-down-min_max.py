"""In this exercise, you’ll develop a function that finds the minimum or
maximum value in a list, depending on the caller’s request.

a. Write a loop (including initialization) to find both the minimum value
in a list and that value’s index in one pass through the list.

b. Write a function named min_index that takes one parameter (a list) and
returns a tuple containing the minimum value in the list and that
value’s index in the list.

c. You might also want to find the maximum value and its index. Write
a function named min_or_max_index that has two parameters: a list and
a bool. If the Boolean parameter refers to True, the function returns a
tuple containing the minimum and its index; if it refers to False, it
returns a tuple containing the maximum and its index.
"""
def min_or_max(list, flag):
    """(list, bool) -> (object, int)
    Returns the min or max value from a given list. Also returns index position if user specifies True as the second argument. Output is determined by user's response which can be either
    min, max, or both.
    given_list = [1, 2, 3]
    >>> Would you like the minimum, maximum, or both values from this list? Please type min, max, or both for your answer.
    >>> both.
    1 is the smallest value, and 3 is the largest.
    """
    # Ask user if they would like the min, max, or both values.
    user_request = input('Would you like the minimum, maximum, or both values from this list? Please type min, max, or both for your answer: ').lower()

    # Based on user selection, lookup and return the corresponding values.
    if user_request == 'min':
        min_value = min(list)
        answer = f'You\'ve chosen the minimum value. It is {min_value}.'
        if flag:
            answer += f' The index of your value is {list.index(min_value)}'
    elif user_request == 'max':
        max_value = max(list)
        answer = f'You\'ve chosen the maximum value. It is {max_value}'
        if flag:
            answer += f' The index of your value is {list.index(max_value)}'
    elif user_request == 'both':
        min_value = min(list)
        max_value = max(list)
        answer = f'You\'ve chosen both values. The min is {min_value} and the maximum value is {max_value}.'
        if flag:
            answer += f' The indices of your values are {list.index(min_value)} and {list.index(max_value)}'

    print(answer)
   

min_or_max([1, 2, 3, 4, 5], True)