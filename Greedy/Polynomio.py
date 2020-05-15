def solve(str) :
    
    L = []
    xCount = 0
    p = list(str)
    p.append('')
    for i in range(len(p)) :
        
        if p[i] == 'X' :
            xCount += 1
            continue
        
        if xCount % 2 == 1 :
            return -1

        while xCount >= 4 :
            L.append('AAAA')
            xCount = xCount - 4
            

        while xCount >= 2 :
            L.append('BB')
            xCount = xCount - 2
            
        if p[i] == '.' :
            L.append('.')
            
    result = ''.join(L)
    return result

P = str(input())
show = print(solve(P))
