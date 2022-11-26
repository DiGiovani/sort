def main(dataset: list[list]):
    quick_sort(dataset, 0, len(dataset) - 1)

def partition(dataset: list[list], start: int, end: int):
	pivot = dataset[end]
	i = start - 1
	
	for j in range(start, end):
		if dataset[j][0] <= pivot[0]:
			i = i + 1
			(dataset[i], dataset[j]) = (dataset[j], dataset[i])

	(dataset[i + 1], dataset[end]) = (dataset[end], dataset[i + 1])

	return i + 1


def quick_sort(array: list[list], start: int, end: int):
	if start < end:
		pi = partition(array, start, end)
		quick_sort(array, start, pi - 1)
		quick_sort(array, pi + 1, end)
