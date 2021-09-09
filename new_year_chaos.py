def minimumBribes(q):
    bribes = 0
    for n in range(len(q)):
        if q[n] - (n + 1) > 2:
            print('Too chaotic')
            return
        
        s = max(0, q[n] - 2)
        
        for m in range(s, n):
            if q[m] > q[n]:
                bribes += 1
                
    print(bribes)        
     


    