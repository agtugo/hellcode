def two_pointers(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        if condition(arr[left], arr[right]):
            # process elements
            pass
        left += 1
        right -= 1