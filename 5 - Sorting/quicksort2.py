def quicksort2(arr):
  if len(arr) <=1 :
     return arr
  else:
     pivot = arr[0]
     less_than_pivot = [x for x in arr[1:] if x <= pivot]
     bigger_than_pivot = [x for x in arr[1:] if x > pivot]
     return quicksort2(less_than_pivot) + [pivot] + quicksort2(bigger_than_pivot)




arr = [0,3,6,7,8,4,2,1,5]


arr = quicksort2(arr)

print(arr)