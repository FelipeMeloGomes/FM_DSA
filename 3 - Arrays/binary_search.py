def binary_search(nums, n, lo, hi):
  lo = 0
  hi = len(nums)

  while lo < hi:
    mid = int((lo+hi)/2)

    if nums[mid] == n:
      return mid
    elif nums[mid] < n:
      lo = mid + 1
    else:
      hi = mid
  return -1
