#[?] 원본 데이터 중에서 대상 데이터와 가장 가까운 값
import sys

# 근삿값 알고리즘: 가장 가까운 값 -> ㅣ원본과 대상과의 차잇값ㅣ의 최솟값

def main():
    #[0] Init(초기화):
    min = sys.maxsize # ㅣ차잇값ㅣ의 최솟값을 저장할 변수
    
    #[1] Input(입력):
    numbers = [ 10, 23, 34, 56, 41, 77 ]
    target = 25 # target과 가까운 값
    near = 0 # 가까운 값
    N = len(numbers)

    #[2] Process(처리): 주어진 범위에 주어진 조건 (필터링)
    for i in range(0, N): # 주어진 범위
        _abs = abs(numbers[i] - target) # ㅣ차잇값ㅣ
        if min > _abs:
            min = _abs # MIN
            near = numbers[i] # NEAR

    #[3] Output(출력):
    print(f'{target}와/과 가장 가까운 값: {near} (차이: {min})')

if __name__ == "__main__":
    main()

#[!] 디버거 사용하기: F9 -> F5-> F11 -> F5