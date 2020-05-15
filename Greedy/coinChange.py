def solve(W) :

    change = W
    n500 =0
    n100 =0
    n50 =0
    n10 =0
    n1 =0
    total = 0
    
    while change >= 500 :
        change = change - 500
        n500 += 1
    
    while change >= 100 :
        change = change - 100
        n100 += 1
       
    while change >= 50 :
        change = change - 50
        n50 += 1
    
    while change >= 10 :
        change = change - 10
        n10 += 1
    
    while change >= 1 :
        change = change - 1
        n1+= 1

    total = n500 + n100 + n50 + n10 + n1

    return(total)
