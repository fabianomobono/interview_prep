# look through already sorted arr

# divide array, if the midpoint is lower than the target, we check the right side if higher we test the left side
# the search ends when the midpoint is same as the target


def binary_search(arr, target):
  begin = 0
  end = len(arr) - 1

  while begin <= end:
    midpoint = begin + (end - begin) // 2

    midpoint_value = arr[midpoint]

    if midpoint_value == target:
      return midpoint

    elif target < midpoint_value:
      end = midpoint - 1

    else:
      begin = midpoint + 1
  return None


a = [1,2,3,4,5,6,7,8,9,10]
b = 10

print(binary_search(a,b))