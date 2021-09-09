l = [1,2,3,4,5,6,7,8,9,10]

t = 6

def two_sum(arr, target):
    d = {}
    
    for x in range(len(arr)):
        if target - arr[x] in d:
            print(x, d[target - arr[x]] )
        
        else:
            d[arr[x]] = x

two_sum(l,t)