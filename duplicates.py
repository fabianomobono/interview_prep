d = [1, 2, 3, 6, 3, 6, 1, 1]

# find all duplicates
def find_duplicates(arr):
  di = set()
  duplicates = set()
  
  for x in arr:
    if x in di:
      
      duplicates.add(x)
    else:
      di.add(x)
  return duplicates

print(find_duplicates(d))
