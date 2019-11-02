def product_of_elements(arr):
    """
        Given an array of integers, return a new array such
        that each element at index i of the new array is
        the product of all the numbers in the original array except the one at i.
    """
    if len(arr) <= 2:
        return False

    result = []
    value = None
    for i in range(len(arr)):
        product = 1
        value = arr[i]
        for num in arr:
            if num == value:
                continue
            else:
                product *= num
        result.append(product)
    return result