def selection_sort():
    arr = input("Ingrese los números a ordenar separados por espacios: ").split()
    arr = [int(x) for x in arr]  # Convierte los elementos de la lista en enteros
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Intercambia los elementos
    return arr

print(selection_sort())

## Brandon Morales  https://www.instagram.com/lewenn19/