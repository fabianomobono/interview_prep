a = [1,2,3,4,5,6,8,9,10]


def missing(arr):
  
  for x in range(len(arr) - 1):
    if arr[x] + 1 != arr[x + 1]:
      print(arr[x] + 1)


missing(a)