T = int(input())
for tc in range(1, T+1):
    N = int(input())
    Nums = input()

    max_count = 1
    count = 1

    for i in range(N-1):
        if Nums[i] == '1':
            if Nums[i] == Nums[i+1]:
                count += 1
                if count > max_count:
                    max_count = count
        elif Nums[i] == '0':
            count = 1

    print(f'#{tc} {max_count}')