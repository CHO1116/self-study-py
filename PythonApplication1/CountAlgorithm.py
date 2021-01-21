#[?] 1부터 1000까지의 정수 중 13의 배수의 개수

# 개수 알고리즘: 주어진 범위에 주어진 조건에 해당하는 자료들의 개수

#[1] Input(입력):
count = 0 # 개수를 저장할 변수

#[2] Process(처리): 주어진 범위에 주어진 조건 (필터링)
for i in range(1, 1001): # 주어진 범위
    if i % 13 == 0: # 주어진 조건(13의 배수 필터링)
        count += 1
        if count < 10:
            print(f' {count}번째 13의 배수: {i}', end = '\n')
        else:
            print(f'{count}번째 13의 배수: {i}', end = '\n')

#[3] Output(출력):
print(f'1부터 1000까지의 정수 중 13의 배수의 개수: {count}')

#[!] 디버거 사용하기: F9 -> F5-> F11 -> F5