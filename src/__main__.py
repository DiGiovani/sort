from pathlib import Path
import cProfile, csv

from .selection_sort import selection_sort
from .insertion_sort import insertion_sort
from .merge_sort import main as merge_sort
from .quick_sort import main as quick_sort


sort_arr: list = [selection_sort, insertion_sort, merge_sort, quick_sort]
order_arr = ["crescente.csv", "decrescente.csv", "random.csv"]
size_arr = ["1000", "2000", "3000", "5000"]
header = []
dataset = [] 
    
print("Selecione o tamanho do dataset: \n 0 - 1000 \n 1 - 2000 \n 2 - 3000 \n 3 - 5000")
size = int(input())

print("\nSelecione a ordem do dataset: \n 0 - Crescente \n 1 - Decrescente \n 2 - Aleatória")
order = int(input())

print(f"{size} - {order}")

with open(f"{Path().absolute()}/datasets/{size_arr[size]}/{order_arr[order]}") as file:
    reader = csv.reader(file)
    header = next(file)
    for row in file:
        dataset.append(row.replace("\n", "").split(","))

print("LISTA DESORDENADA")
print("------------------------------------------------------------------------------------------------------------------------------------------")

for row in dataset:
    print(row)

print("Selecione o método de ordenação: \n0 - Ordenação por seleção\n1 - Ordenação por inserção\n2 - Ordenação por intercalação\n3 - Ordenação rápida")
sorting = int(input())
swipes = 0
print("------------------------------------------------------------------------------------------------------------------------------------------")
cProfile.run("swipes = sort_arr[sorting](dataset)")
print("------------------------------------------------------------------------------------------------------------------------------------------")

print("LISTA ORDENADA")
print("------------------------------------------------------------------------------------------------------------------------------------------")

for row in dataset:
    print(row)
