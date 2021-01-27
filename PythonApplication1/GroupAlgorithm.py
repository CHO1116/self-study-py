#[?] 컬렉션 형태의 데이터를 특정 키 값으로 그룹화
from random import *
# 그룹 알고리즘: 특정 키 값에 해당하는 그룹화된 합계 리스트 만들기

# 테스트용 레코드 클래스
class Record():
	def __init__(self, name, quantity):
		self.name = name # 상품명
		self.quantity = quantity # 수량

def main():
	#[0] Init(초기화): 
	records = []

	#[1] Input(입력): 
	f = open('testcase.txt', 'r') # (응용) 파일로 입력받기
	while True:
		#name = input("무엇이 있나요? > ") # (기초) 직접 입력시키기
		#quantity = int(input("얼마나 있나요? > ")) # 직접 입력시키기
		name = f.readline() # 불러온 파일에서 한 line씩 read하는 함수
		quantity = randint(1, 50) # 수량 랜덤 입력
		if not name:
			break
		records.append(Record(name, quantity)) # 클래스로 배열에 저장
	f.close() # 파일 닫기
	groups = [] # 출력 데이터
	N = len(records)

	#[2] Process(처리): Sort -> Sum -> Group
	#[A] Sort - Selection Sort (ASC)
	for i in range(0, N-1): # (ASC) 문자열의 Sort는 대문자 먼저 오름차순 정리되고 소문자 정리
		for j in range(i + 1, N):
			if records[i].name > records[j].name:
				temp = records[i].name
				records[i].name = records[j].name
				records[j].name = temp

	#[B] Group - 그룹 소계
	subtotal = 0
	for i in range(N):
		subtotal += records[i].quantity # 같은 상품명의 수량을 누적(SUM)
		#[!] 다음 레코드가 없거나(i+1이 N이거나) 현제 레코드와 다음 레코드가 다르면 저장
		if (i + 1) == N or records[i].name != records[i + 1].name:
			# 한 그룹의 키(key) 지정, 소계
			groups.append(Record(records[i].name, subtotal)) # 하나의 그룹 저장
			subtotal = 0

	#[3] Output(출력): 
	print('[1] 정렬된 원본 데이터: ')
	for r in records:
		print(f'    Name : {r.name}' + f'Quantity : {r.quantity}')

	print('이름으로 그룹화된 데이터: ')
	for g in groups:
		print(f'    Name : {g.name}' + f'Quantity : {g.quantity}')

if __name__ == "__main__":
	main()

#[!] 디버거 사용하기: F9 -> F5-> F11 -> F5