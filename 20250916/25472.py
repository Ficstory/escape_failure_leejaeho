T = int(input())
for tc in range(1, T+1):
    N = int(input())
    dic = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
    # 16진수 표기대응 딕셔너리
    total = 0
    # 합계를 받아줄 변수 
    ox = input()
    for j in ox:
        if j in '0123456789':
            # 0~9면 
            total += int(j)
            # 바로 더해주고
        elif j in 'ABCDEF':
            # 문자면
            total += dic[j]
            # 딕셔너리 키값으로 넣고 더해줌
    print(f'#{tc} {total}')


        


    
