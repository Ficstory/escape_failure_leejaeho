"""
같은 줄에 1 에서 9 까지의 숫자를 한번씩만 넣고,
 3 x 3 크기의 작은 격자 또한,
1 에서 9 까지의 숫자가 겹치지 않아야 한다.

입력으로 9 X 9 크기의 스도쿠 퍼즐의 숫자들이 주어졌을 때,
위와 같이 겹치는 숫자가 없을 경우,
1을 정답으로 출력하고 그렇지 않을 경우 0 을 출력한다.
"""

T = int(input())
# 테스트 케이스수 받아오기
for tc in range(1, T + 1):
    sdoku = [list(map(int, input().split())) for _ in range(9)]

    # 9칸안에 1~ 9까지의 수가 다 있는지 어떻게 검사할 것인가?
    # set으로 만들고 중복제거된 길이가 9보다 작은가?
    # 그럼 가로축으로 한번 세로축으로 한번, 박스권 한번 총 3번 반복을 돌려야겠네

    answer = True
    # 처음에 트루로 놓고 조건 안맞으면 false로 바꿈

    for i in range(9):
        # 가로열 먼저
        path = []
        # 간이 리스트 하나 만들어주고
        for j in range(9):
            path.append(sdoku[i][j])
            # 리스트에 한줄 담은 다음에
            test = set(path)
            # set에 모아가지고
        if len(test) < 9:
            answer = False
            #길이 검사

    for j in range(9):
        # 세로열 검사
        path = []
        for i in range(9):
            path.append(sdoku[i][j])
            test = set(path)
        if len(test) < 9:
            answer = False
            # 구조는 똑같고 i, j 반복순서만 바꿈

    for w in range(3):
        # 3*3 칸에 잘 있는지 확인
        # 3*3 칸 마다 왼쪽 상단을 기준점으로 잡고 
        # 기준점마다 옮겨 다니는 반복문
        for v in range(3):
            path = []
            # 박스 하나 검사할때 마다 초기화 될수 있도록 간이리스트 위치 설정
            for i in range(3):
                for j in range(3):
                    path.append(sdoku[3*w+i][3*v + j])
                    # 하나씩 담아주고
            test = set(path)
            if len(test) < 9:
                answer = False
                # 검사하고
                

    print(f'#{tc} {int(answer)}')
    # 마지막 출력해보면 검사 끝





