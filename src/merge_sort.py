def main(dataset: list[list]):
	merge_sort(dataset, 0, len(dataset)-1)

def merge(arr: list[list], start: int, mid: int, end: int):
	left_size = mid - start + 1
	right_size = end - mid

	left = [[]] * left_size
	right = [[]] * right_size
	
	for i in range(0, left_size):
		left[i] = arr[start + i]

	for j in range(0, right_size):
		right[j] = arr[mid + 1 + j]
		
	i = 0	 
	j = 0	 
	k = start	 

	while i < left_size and j < right_size:
		if left[i][0] <= right[j][0]:
			arr[k] = left[i]
			i += 1
		else:
			arr[k] = right[j]
			j += 1
		k += 1

	while i < left_size:
		arr[k] = left[i]
		i += 1
		k += 1
		
	while j < right_size:
		arr[k] = right[j]
		j += 1
		k += 1

def merge_sort(arr: list[list], left: int, right: int):
	if left < right:
		mid = left+(right-left)//2
		
		merge_sort(arr, left, mid)
		merge_sort(arr, mid+1, right)
		merge(arr, left, mid, right)
