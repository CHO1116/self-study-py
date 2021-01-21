#[?] 주어진(지정한 범위) 데이터의 순위를 구하는 로직
import sys

# 순위 알고리즘: 점수 데이터에 대한 순위 구하기

def main():
    #[0] Init(초기화):
    rankings = [1] * 15 # 모두 1로 초기화

    #[1] Input(입력):
    scores = [25, 34, 55, 62, 17, 30, 41, 63, 66, 70, 100, 33, 88, 91, 15]
    # 등수    13  10   8   7  14  12   9   6   5   4   1   11   3   2  15
    N = len(scores)

    #[2] Process(처리): 주어진 범위에 주어진 조건 (필터링)
    for i in range(N): # 주어진 범위
        rankings[i] = 1 # 1등으로 초기화, 순위배열을 매 회전마다 1등으로 초기화
        for j in range(N):
            if scores[i] < scores[j]: # 현재(i)와 나머지들(j) 비교
                rankings[i] += 1 # (i)의 등수가 하나씩 내려감

    #[3] Output(출력):
    for i in range(N):
        print(f'{scores[i]:3}점: {rankings[i]}등')

if __name__ == "__main__":
    main()

#[!] 디버거 사용하기: F9 -> F5-> F11 -> F5