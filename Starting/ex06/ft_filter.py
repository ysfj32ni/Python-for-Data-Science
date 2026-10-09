def ft_filter(function, iterable):
    """Return the items from iterable for which function returns true."""
    return [item for item in iterable if function(item)]
