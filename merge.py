import time

def merge(left, right, descending=False):
    """ Helper function for merging two halves """
    merged = []
    while left and right:
        if (left[0] < right[0] and not descending) or (left[0] > right[0] and descending):
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    merged.extend(left or right)
    return merged

def merge_sort_recursive(arr, descending=False):
    """ Recursive merge sort that supports both ascending and descending order """
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort_recursive(arr[:mid], descending)
    right = merge_sort_recursive(arr[mid:], descending)
    return merge(left, right, descending)

def merge_sort_iterative(arr, descending=False):
    """ Iterative merge sort that also supports both ascending and descending order """
    width = 1
    n = len(arr)
    while width < n:
        i = 0
        while i < n:
            left = arr[i:i + width]
            right = arr[i + width:min(i + 2 * width, n)]
            arr[i:i + len(left) + len(right)] = merge(left[:], right[:], descending)
            i += 2 * width
        width *= 2
    return arr

def measure_time(func, arr, desc):
    """ Function to measure the execution time of sorting function """
    start = time.time()
    sorted_arr = func(arr[:], desc)  # Make a copy of the array to avoid in-place sorting issues
    end = time.time()
    return sorted_arr, end - start

def main():
    # Meminta input dari pengguna
    input_str = input("Masukkan elemen array: ")
    user_array = list(map(int, input_str.split()))

    # Ascending and Descending with both methods
    sorted_asc_iter, time_asc_iter = measure_time(merge_sort_iterative, user_array, False)
    sorted_desc_iter, time_desc_iter = measure_time(merge_sort_iterative, user_array, True)
    sorted_asc_rec, time_asc_rec = measure_time(merge_sort_recursive, user_array, False)
    sorted_desc_rec, time_desc_rec = measure_time(merge_sort_recursive, user_array, True)

    print("\nMetode | Urutan     | Waktu Eksekusi (detik) | Array yang Diurutkan")
    print("-"*80)
    print(f"Iteratif | Ascending  | {time_asc_iter:.6f} | {sorted_asc_iter}")
    print(f"Iteratif | Descending | {time_desc_iter:.6f} | {sorted_desc_iter}")
    print(f"Rekursif | Ascending  | {time_asc_rec:.6f} | {sorted_asc_rec}")
    print(f"Rekursif | Descending | {time_desc_rec:.6f} | {sorted_desc_rec}")

if __name__ == "__main__":
    main()
