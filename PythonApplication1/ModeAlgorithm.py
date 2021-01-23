#[?] 100명의 학생들이 선호하는 숫자를 알아보기 위해 0~9 사이의 숫자를 선택해 제출하도록 하였다.(숫자는 랜덤함수를 통해 입력)
#	 각 학생들은 제출한 순서대로 번호를 부여하여 익명으로 처리된다.
#	 입력된 숫자들 중 가장 많은 학생들이 선택한 숫자는 무엇이고, 몇 명이 골랐는지 알아보자.
from random import *
import sys
# 최빈값 알고리즘: 

def main():
	#[0] Init(초기화):
	max = -sys.maxsize - 1 # 최빈값
	mode = 0 # 빈도  수
	data = [0] * 100 # 100명의 학생들이 제출한 점수들이 저장되는 공간
	index = [0] * 10 # 0~9점의 점수 인덱스의 개수가 저장되는 공간
	cnt = 0 # 빈도 수가 동일 한 경우에 사용

	#[1] Input(입력):
	N = len(data) # 의사코드
	M = len(index) # 의사코드

	print('\n ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100명의 학생들이 제출한 숫자는 다음과 같습니다.━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━', end = '\n\n')
	for x in range(N): #
		num = randint(0, 9) # 각 학생들의 점수는 랜덤으로 생성
		data[x] = num # 배열에 점수들을 각각 저장 DATA
		if x % 4 == 0:
			print('┃', end = '\t')
		print(f'{x:2}번 학생이 제출한 숫자: {data[x]:2}', end = '\t')
		if (x + 1) % 4 == 0: # 화면에 출력되는 모양의 가독성을 높이기 위함
			print('┃\n')
	print(' ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n')

	#[2] Process(처리): Data -> Index -> Count -> Max -> Mode
	for a in range(0, N - 1): # ASC Sort Algorithm
		for b in range(a + 1, N):
			if data[a] > data[b]:
				temp = data[a]; data[a] = data[b]; data[b] = temp

	print('\n ━━━━━━━━━━━━━━━━━━━━━ 학생들이 고른 숫자를 오름차순으로 정렬합니다.━━━━━━━━━━━━━━━━━━━━')
	for i in range(N):
		if i % 10 == 0:
			print('┃', end = '\t')
		print(data[i], end = '\t')
		if (i + 1) % 10 == 0:
			print('┃\n')
	print(' ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n')

	for j in range(N):
		index[data[j]] += 1 # COUNT

	for k in range(M):
		if max < index[k]:
			max = index[k] # MAX
			mode = k # MDOE
	for num in range(M): # 중복된 최빈값이 있는지 탐색
		if max == index[num]:
			cnt += 1

	if cnt > 1: # 중복이 있으면 모두 표현해줄 수 있도록 진행
		samescore = [0] * cnt
		cnt = 0
		for num in range(M):
			if max == index[num]:
				sametime = index[num]
				samescore[cnt] = num
				cnt += 1

	#[3] Output(출력):
	print('\n ━━━━━━━━━━━━━━━━━━━━━━ 각 점수를 고른 학생들의 수━━━━━━━━━━━━━━━━━━━━━━')
	for i in range(M):
		if i % 2 == 0:
			print('┃', end = '\t')
		print(f'{i}점을 고른 학생의 수: {index[i]:2}명', end = '\t')
		if (i + 1) % 2 == 0:
			print('┃\n')
	print(' ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n')

	if cnt == 1:
		print(f'\n가장 많이 나온 점수는 {mode}점이고, {mode}점을 고른 학생의 수는 {max}명입니다.\n')
	if cnt > 1:
		print('\n가장 많이 나온 점수는', end = ' ')
		for idx in range(cnt):
			print(f'{samescore[idx]}점', end = ' ')
		print(f'이고, 각 점수를 고른 학생의 수는 각각 {sametime}명씩입니다.\n')

if __name__ == "__main__":
	main()

#[!] 디버거 사용하기: F9 -> F5-> F11 -> F5