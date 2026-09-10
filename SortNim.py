def InsertRecursive(sorted_array, current_value, current_length):
    if current_length == 0 or sorted_array[current_length - 1] <= current_value:
        sorted_array[current_length] = current_value
        return

    sorted_array[current_length] = sorted_array[current_length - 1]

    InsertRecursive(sorted_array, current_value, current_length - 1)


def RecursiveFilterSort(data_array, current_length):
    if current_length == 0:
        return []

    sorted_array = RecursiveFilterSort(data_array, current_length - 1)
    current_value = data_array[current_length - 1]

    if int(NIM_MAHASISWA[-1]) % 2 == 0:
        if current_value % 2 == 0:
            sorted_array.append(0)
            InsertRecursive(sorted_array, current_value, len(sorted_array) - 1)
    else:
        if current_value % 2 != 0:
            sorted_array.append(0)
            InsertRecursive(sorted_array, current_value, len(sorted_array) - 1)
    return sorted_array


NIM_MAHASISWA = "71251181"

if NIM_MAHASISWA != "":
    raw_data = [int(digit) for digit in NIM_MAHASISWA]
    data_length = len(raw_data)

    final_result = RecursiveFilterSort(raw_data, data_length)

    print("===== FILTER & SORT NIM =====")
    print("NIM Mahasiswa :", NIM_MAHASISWA)

    if int(NIM_MAHASISWA[-1]) % 2 == 0:
        print("Tipe          : GENAP (Ascending)")
    else:
        print("Tipe          : GANJIL (Ascending)")

    print("Data Digit Awal :", raw_data)
    print("Hasil Akhir   :", final_result)