def find_unsorted_subarray(arr):
    n = len(arr)

    # edgecases
    if all(arr[i] <= arr[i + 1] for i in range(n - 1)) or all(arr[i] >= arr[i + 1] for i in range(n - 1)):
        return [0, 0]

    # Find the start of the unsorted subarray
    start = 0
    while start < n - 1 and arr[start] <= arr[start + 1]:
        start += 1

    # Find the end of the unsorted subarray
    end = n - 1
    while end > 0 and arr[end] >= arr[end - 1]:
        end -= 1

    # Find the minimum and maximum values in the unsorted subarray
    min_value = min(arr[start:end + 1])
    max_value = max(arr[start:end + 1])

    # Expand the unsorted subarray to include any additional elements that need to be sorted
    while start > 0 and arr[start - 1] > min_value:
        start -= 1
    while end < n - 1 and arr[end + 1] < max_value:
        end += 1

    return [start, end]


