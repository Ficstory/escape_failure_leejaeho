
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    max_danjo = -1

    for i in range(N):
        for j in range(i+1,N):
            danjoni = nums[i] * nums[j]
            str_danjoni = str(danjoni)
            for c in range(len(str_danjoni)-1):
                if str_danjoni[c] > str_danjoni[c+1]:
                   break                
            else:
                if danjoni > max_danjo:
                    max_danjo = danjoni
    
        
    print(f'#{tc} {max_danjo}')