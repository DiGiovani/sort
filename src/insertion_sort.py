def swipe(dataset: list[list], major_index: int, minor_index: int):
    aux = dataset[major_index]
    dataset[major_index] = dataset[minor_index]
    dataset[minor_index] = aux

def insertion_sort(dataset: list[list[str]]):
    for i in range(1, len(dataset)):
        j = i
        while((j > 0) and (dataset[j][0] < dataset[j-1][0])):
            if dataset[j][0] < dataset[j-1][0]:
                swipe(dataset, major_index=j, minor_index=j-1)
                j = j - 1
