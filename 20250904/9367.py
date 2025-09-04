T = int(input())
for tc in range(1, T+1):
    N = int(input())
    carrot = list(map(int, input().split()))

    max_count = 1
    bigger_count = 1
    for i in range(N-1):
        if carrot[i] < carrot[i+1]:
            bigger_count += 1
            if max_count < bigger_count:
                max_count = bigger_count 
        elif carrot[i] >= carrot[i+1]:
            bigger_count = 1
        
    print(f'#{tc} {max_count}')


