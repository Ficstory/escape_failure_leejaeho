T = int(input())
# 테스트 케이스 수를 받아옴
for tc in range(1, T+1):
    # 테케 반복
    char = input()
    # 문자열로 받아옴
    count = 0
    # 바꿀때마다 +1 할수 있는 카운트 초기화
    for i in range(len(char)):
        # 문자열 길이만큼 반복      
        if i < len(char)-1:
            # i가 n-1이 되면 인덱스 에러나서 i가 길이 -1일때까지만 반복
            if char[i] != char[i+1]:
                # 결국 1에서 0으로 몇번 바뀌는지는 인덱스 앞 뒤로
                # 같은지 다른지만 보면됨         
                count += 1
                # 다르면 +1
    if char[0] == '1':
        count += 1
        # 첫 글자가 1이면 한번 누르고 시작해야해서 1 추가함

    print(f'#{tc} {count}')


