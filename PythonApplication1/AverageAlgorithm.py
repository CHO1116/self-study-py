#[?] n명의 점수 중에서 80점 이상 95점 이하인 점수의 평균

# 평균 알고리즘: 주어진 범위에 주어진 조건에 해당하는 자료들의 평균

#[1] Input(입력):
data = [90, 65, 75, 88, 54, 79, 81, 12, 77, 94, 91, 97, 33, 86, 87]
count = 0 # 개수를 저장할 변수
sum = 0 # 합계를 저장할 변수
avg = 0 # 평균을 저장할 변수

#[2] Process(처리): AVG = SUM / COUNT
N = len(data)
print(f'자료의 총 개수: {N}\n')
for i in range(0, N): # 주어진 범위
    if 80 <= data[i] <=95: # 주어진 조건
        sum += data[i] # SUM
        count += 1 # COUNT

try: # 0으로 나누는 경우는 예외 처리가 되도록 처리
    avg = sum / count # AVG
except ZeroDivisionError as e:
    print(e)

#[3] Output(출력):
print(f'80점 이상 95점 이하인 자료들의 평균: {avg:.2f}')

#[!] 디버거 사용하기: F9 -> F5-> F11 -> F5