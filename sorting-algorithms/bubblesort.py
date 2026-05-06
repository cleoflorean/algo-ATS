def bubble_sort(data):
    n = len(data)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True

        # Optimasi: berhenti jika tidak ada pertukaran
        if not swapped:
            break

    return data


if __name__ == "__main__":
    angka = [64, 34, 25, 12, 22, 11, 90]

    print("Data sebelum sorting:")
    print(angka)

    hasil = bubble_sort(angka)

    print("\nData setelah sorting:")
    print(hasil)