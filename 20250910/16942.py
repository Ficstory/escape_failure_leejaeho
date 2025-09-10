
def partition(left, right):
    p = arr[left]
    i = left + 1
    j = right

    while i <= j:
        while i <= j and arr[i] <= p:
            i += 1
        while i <= j and arr[j] >= p:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[left], arr[j] = arr[j], arr[left]

    return j


def quick_sort(left, right):
    if left < right:
        p_idx = partition(left, right)
        quick_sort(left, p_idx - 1)
        quick_sort(p_idx + 1, right)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    quick_sort(0, N-1)

    print(f'#{tc} {arr[N//2]}')
    


