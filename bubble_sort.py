'''' 
This is bubble sort in python created by Avinash 
'''
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):

        for j in range(0, n-i-1):
            
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
arr = [2,1,7,3,5,10,4]

print("Original:", arr)
print("Sorted:", bubble_sort(arr))