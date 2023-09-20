#----------Bubble Sort
def bubble_sort(data, n):
    for i in range(0, n):
        for j in range(0, n - 1 - i):
            if data[j] > data[j + 1]:
                temp = data[j]
                data[j] = data[j + 1]
                data[j + 1] = temp
    return data

data = input("Enter a list of numbers, separated by spaces: ")
data = [int(x) for x in data.split()]  
n = len(data)
result = bubble_sort(data, n)
print("The sorted list is:", result)

#-------- Selection Sort ---------

def selection_sort(data, n):
    for i in range(0, n):
        min_index = i
        for j in range(i + 1, n):
            if data[j] < data[min_index]:
                min_index = j
        temp = data[i]
        data[i] = data[min_index]
        data[min_index] = temp
    return data

data = input("Enter the list of numbers separated by spaces: ").split()
data = [int(num) for num in data]
n = len(data)
result = selection_sort(data, n)
print("The sorted list is:", result)

# ----------- Insertion Sort 

def insertionSort(list):
    N = len(list)
    for index in range(1,N):
        current_element  = list[index]
        pos = index - 1
        while current_element <= list[pos]:
            list[pos + 1] = list[pos]
            pos  = pos - 1
        list[pos]= current_element

list = [5,6,9,1,2,10,25,12,11]
insertionSort(list)
print(list)
