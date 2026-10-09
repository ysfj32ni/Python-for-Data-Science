def ft_filter(function, iterable):
    """
    Filters an iterable based on a function.
    Args:
        function (__call__): The function to apply
        to each item in the iterable.
        iterable (_type_): The iterable to filter.
    Returns:
        _type_: The filtered iterable.
    """
    return [item for item in iterable if function(item)]
