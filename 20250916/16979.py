"""
A사는 여러 곳에 공장을 갖고 있다. 
봄부터 새로 생산되는 N종의 제품을 
N곳의 공장에서 한 곳당 한가지씩 생산하려고 한다.

각 제품의 공장별 생산비용이 주어질 때
전체 제품의 최소 생산 비용을 계산하는 프로그램을 만드시오.

예를 들어 3개의 제품을 생산하려는 
경우 각 공장별 생산비용은 다음과 같이 주어진다..
"""


def solve(idx, plus):
    global min_sum
    if plus >= min_sum:
        return
    # 가지치기 : 중간에 최솟값보다 커지면 더 볼 필요없이 중간

    if idx == N:
        if plus < min_sum:
            min_sum = plus
    # 중단조건 : N개의 상품을 다 골랐을때 중단하면서 최소 생산비용인지 확인
     
    for i in range(N):
        if visited[i] == False:
            visited[i] = True
            solve(idx + 1, plus+arr[idx][i])
            visited[i] = False
    # 재귀호출 : 반복문, 재귀를 통해 모든 제품을 모든공장에서 생산하고 값을 비교함
    # 재귀호출 끝나면 방문했던 곳을 다시 원래대로 되돌림


# 순열문제
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_sum = 9999999999999
    # 최솟값 크게 설정
    visited = [False] * N
    # 방문배열 설정
    solve(0,0)
    # idx = 고른 상품의 개수
    # plus = 누적합계
    
    print(f'#{tc} {min_sum}')