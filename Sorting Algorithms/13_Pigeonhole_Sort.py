def pigeonhole_sort(arr):
    min_val = min(arr)
    max_val = max(arr)
    size = max_val - min_val + 1

    holes = [0] * size

    for x in arr:
        holes[x - min_val] += 1

    i = 0
    for count in range(size):
        while holes[count] > 0:
            holes[count] -= 1
            arr[i] = count + min_val
            i += 1
    return arr

# Example usage
arr = [8, 3, 2, 7, 4, 6, 8]
print("Sorted array is:", pigeonhole_sort(arr))
