def solve(G,C) :
    L = []
    w = 0
    v = 0
    S = []
    for i in range(len(G)) :
        x = G[i][1] / G[i][0]
        G[i].insert(0, x)

    S = sorted(G)
    S.reverse()

    while S :
        if w == C :
            break
        
        while w + S[0][1] <= C :
            L.append(S[0])
            w = w + S[0][1]
            v = v + S[0][2]
            del S[0]

        if C - w > 0 :
            a = C -w
            b = a * S[0][0]
            S[0][1] = a
            S[0][2] = b
            L.append(S[0])
            v = v + S[0][2]
            del S[0]
            break
        
    for i in range(len(L)) :
        del L[i][0]
        
    return L, v
