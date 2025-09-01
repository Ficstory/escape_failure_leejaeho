T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    # N : 학생수, K : 찾아야하는 학생 번호
    score = [list(map(int, input().split())) for _ in range(N)]
    # 학생별로 받은 점수 인덱스 순서로 중간고사, 기말고사, 과제

    # 문제에서 N명의 학생이 있을경우 N/10명의 학생들에게 동일한 평점을 부여할 수 있다고 함
    # 따라서 10명이면 각 학점별로 1명씩만 줄 수 있음
    # 일단 최종 스코어를 정리하는 리스트가 필요
    li = []
    for i in range(N):
        # i는 사람의 인덱스
        mid_test = score[i][0]
        last_test = score[i][1]
        homework = score[i][2]
        # 각각의 점수를 변수로 받고 각 점수를 계산
        total_score = mid_test * 0.35 + last_test * 0.45 + homework * 0.2
        # 중간, 기말, 과제 비율각각 곱해서 총점 계산
        li.append(total_score)
        # 최종스코어를 리스트로 저장


    count = 0
    for j in range(N):
        # 리스트돌면서 K 보다 점수가 낮은 사람있으면 카운트 +1
        if li[K-1] > li[j]:
            #K보다 점수 낮으면 (문제에서 같은경우 없음)
            count += 1

    K_rank = (N-count)/N * 100
    # 백분률로 계산
    result = ""
    if 0 < K_rank <= 10:
        result = 'A+'
    elif 10 < K_rank <= 20:
        result = 'A0'
    elif 20 < K_rank <= 30:
        result = 'A-'
    elif 30 < K_rank <= 40:
        result = 'B+'
    elif 40 < K_rank <= 50:
        result = 'B0'
    elif 50 < K_rank <= 60:
        result = 'B-'
    elif 60 < K_rank <= 70:
        result = 'C+'
    elif 70 < K_rank <= 80:
        result = 'C0'
    elif 80 < K_rank <= 90:
        result = 'C-'
    elif 90 < K_rank <= 100:
        result = 'D0'

    print(f'#{tc} {result}')









