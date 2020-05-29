def heapSort(A) :
    
    n = len(A)
    A.insert(0, 0)

    for i in range(n, 0, -1) :
        downHeap(A, i, n)

    for i in range(n, 0, -1) :
        A[i], A[1] = A[1], A[i]
        downHeap(A, 1, i-1)


def downHeap(arr, i, n) :

    left = i * 2
    right = i * 2 + 1
    bigger = i

    if left <= n and arr[bigger] < A[left] :
        bigger = left

    if right <= n and arr[bigger] < A[right] :
        bigger = right

    if bigger != i :
        arr[i], arr[bigger] = arr[bigger], arr[i]
        return downHeap(arr, bigger, n)
