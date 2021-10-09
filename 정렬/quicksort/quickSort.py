def quicksort(A, lo_idx, hi_idx):
    def partition(lo_idx, hi_idx):
        left_idx = lo_idx
        pivot = A[hi_idx]
        for right_idx in range(lo_idx, hi_idx):
            if A[right_idx] < pivot:
                A[left_idx], A[right_idx] = A[right_idx], A[left_idx]
                left_idx += 1
        A[left_idx], A[hi_idx] = A[hi_idx], A[left_idx]
        return left_idx

    if lo_idx < hi_idx:
        pivot = partition(lo_idx, hi_idx)
        quicksort(A, lo_idx, pivot - 1)
        quicksort(A, pivot + 1, hi_idx)


A = [2, 8, 7, 1, 3, 5, 6, 4]
A = [1, 2, 3, 4]
A = [4, 3, 2, 1]
quicksort(A, 0, len(A) - 1)
print(A)
