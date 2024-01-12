def bubble_sort(arr, comparison_function):
  sorted = False
  while not sorted:
    sorted = True
    for idx in range(len(arr) - 1):
      if comparison_function(arr[idx], arr[idx + 1]):
        sorted = False
        arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
  return arr


