def binary_search(arr, item, low, high):
    while low <= high:
        mid = (low + high) // 2

        if item == arr[mid]:
            return mid + 1

        elif item > arr[mid]:
            low = mid + 1

        else:
            high = mid - 1

    return low


def binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]

        # Cari posisi menggunakan binary search
        pos = binary_search(arr, key, 0, i - 1)

        # Geser elemen
        j = i

        while j > pos:
            arr[j] = arr[j - 1]
            j -= 1

        arr[pos] = key

    return arr


if __name__ == "__main__":
    angka = [37, 23, 0, 17, 12, 72, 31]

    print("Data sebelum sorting:")
    print(angka)

    hasil = binary_insertion_sort(angka)

    print("\nData setelah sorting:")
    print(hasil)