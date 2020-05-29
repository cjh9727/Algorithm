def bubbleSort(A) :

    for i in range(1, len(A)) :
        for j in range(1, len(A) - i + 1):
            if A[j-1] > A[j] :
                A[j-1], A[j] = A[j], A[j-1]
                print(A)
    return A
