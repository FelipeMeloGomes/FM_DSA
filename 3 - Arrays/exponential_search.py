from binary_search import binary_search


def exponential_search(arr, target):
  if not arr:
      return -1
  if arr[0] == target:
      return 0
  n = len(arr)
  i = 1

  while i < n and arr[i] < target:
    i *= 2

  if i < n and arr[i] == target:
    return i

  return binary_search(arr, target, i//2, min(i, n))


arr =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
       21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
       39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56,
       57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74,
       75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92,
       93, 94, 95, 96, 97, 98, 99, 100]
target = 32
result =  exponential_search(arr, target)

print(f"Element found at index {result}")