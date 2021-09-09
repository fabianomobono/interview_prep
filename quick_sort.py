# find pivot point
# if a number is less than the pivot it goes to the left other it goes to the right
# you can use any number at the beginning

def quick_sort(arr):
  length = len(arr)
  if length <= 1:
    return arr
  else:
    pivot = arr.pop()
  
  items_greater = []
  items_lower = []

  for item in arr:
    if item > pivot:
      items_greater.append(item)

    else:
      items_lower.append(item)

  return  quick_sort(items_lower) + [pivot] + quick_sort(items_greater)


print(quick_sort([9,8,7,6,5,4,3,2,1,120]))