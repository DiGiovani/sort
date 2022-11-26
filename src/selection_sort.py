def swipe(dataset: list[list], major_index: int, minor_index: int):
    aux = dataset[major_index]
    dataset[major_index] = dataset[minor_index]
    dataset[minor_index] = aux

def selection_sort(dataset: list[list[str]]):
    for i in range(len(dataset) - 1):
        menor = i
        for j in range(i+1, len(dataset)):
            if dataset[j][0] < dataset[menor][0]:
                menor = j

        if menor != i:
            swipe(dataset, major_index=i, minor_index=menor)
