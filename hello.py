print("Hello. World!")
print("Hello. World!")

# 문자열

# str 문자열 클래스
# type("Hello. World!")
# <class 'str'>

# type('Hello. World!')
# <class 'str'>


# 이스케이프 문자
# print('C:\Windows\System32\notepad.exe')
# C:\Windows\System32
# otepad.exe

print(r'C:\Windows\System32\notepad.exe')
# C:\Windows\System32\notepad.exe

print('\"It\'s not that I\'m so smart; it\'s just that I stay with problems longer.\" Albert Einstein')
# "It's not that I'm so smart; it's just that I stay with problems longer." Albert Einstein

print('''"It's not that I'm so smart; it's just that I stay with problems longer." Albert Einstein''')
# "It's not that I'm so smart; it's just that I stay with problems longer." Albert Einstein

# 여러 줄에 걸친 문자열을 나타낼 때
print('''Wake up, Neo... 
The Matrix has you...
Follow the white rabbit.''')

# 주석
'''
Wake up, Neo... 
The Matrix has you...
Follow the white rabbit.
'''

# 인덱싱
print('***************인덱싱*****************')
word = 'Python'
print(len(word))
print(word[0])
print(word[0] + word[1] + word[2] + word[3] + word[4] + word[5])

print(word[-6])
print(word[-6] + word[-5] + word[-4] + word[-3] + word[-2] + word[-1])

# 슬라이싱
print('***************슬라이싱*****************')
print(word[:3])
print(word[3:])

# 2.3.2 산술 연산
print('***************산술 연산*****************')
print(1 + 2)
print(3 - 5)
print(5 * 8)
print(2 ** 8)
print(pow(2, 8))
print(5 / 3)
print(5 // 3)  # 몫
print(5 % 3)  # 나머지

x = 2
x += 2
print(x)

# 2.3.3 흐름 제어
print('***************흐름 제어*****************')
# if 조건문
print('***************if 조건문*****************')
rsi = 20
if rsi > 70:
    print('RSI', rsi, 'means overbought.')
elif rsi < 30:
    print('rsi', rsi, 'means oversold.')
else:
    print('...')

# for 반복문
for i in [1, 3, 5]:
    print(i)

for i in range(1, 8, 2):
    print(i)

FAANG = ['FB', 'AMZN', 'AAPL', 'NFLX', 'GOOGL']
for idx, symbol in enumerate(FAANG, 1):
    print(idx, symbol)

# while 반복문
print('***************while 반복문*****************')
i = 1
while i < 7:
    print(i)
    i += 2
print('***************while 반복문*****************')
i = 0
while i >= 0:
    i += 1
    if (i % 2) == 0:
        continue
    if i > 5:
        break
    print(i)
else:
    print('Condition is False.')

# try except 예외 처리
print('***************try except 예외 처리*****************')
try:
    1 / 0
except Exception as e:
    print('Exception occured: ', str(e))

# 2.4 반복 자료형

# 2.4.1 리스트
print('***************try except 예외 처리*****************')
ls = ['one', 'two', 'three', 4, 5, 6]
print(ls)
ls2 = list(['one', 'two', 'three', 4, 5, 6])
print(ls2)

print(ls[0], ls[-1])

L = [[1, 2], [3, 4]]
print(L[0], L[1])

print(L[0][1])
print(L[1][1])

print(L + L)
print(L * 3)

# split() 함수
print('***************split() 함수*****************')
myList = 'Thoughts become things.'.split()
print(type(myList))
print(myList)

# join() 함수
print('***************join() 함수*****************')
print(' '.join(myList))

# append() 와 extend()
print('***************append() 함수*****************')  # 넘겨 받은 인수의 자료형에 상관 없이 리스트 뒤에 그대로 추가
L = [1, 2]
L.append([3, 4])
print(L)
L.append(5)
print(L)

print('***************extend() 함수*****************')  # 넘겨받은 인수가 반복 자료형일 경우, 반복 자료형 내부의 각 원소를 추가
L = [3, 2]
print(L)
L.extend([3, 4])
print(L)
L.extend([5])
print(L)

try:
    L.extend(6)
    print(L)
except Exception as e:
    print('Exception Occured: ', str(e))

L.extend([7])
print(L)

# 구분자 변경하기
print('***************구분자 변경하기*****************')
print('-'.join('2012/01/04'.split('/')))
print('2012/01/04'.replace('/', '-'))

# 천 단위 숫자를 쉼표로 구분하기
print('***************천 단위 숫자를 쉼표로 구분하기*****************')
print('1,234,567,890'.split(','))
print(''.join('1,234,567,890'.split(',')))
print('1,234,567,890'.replace(',', ''))

print(format(1234567890, ','))

# 리스트 복사
print('***************리스트 복사*****************')
myList = ['Thoughts', 'become', 'things.']
newList = myList
print(newList)
newList = myList[:]
print(newList)
newList = myList[:2]
print(newList)
newList = myList[2:]
print(newList)

print('***************swallow copy*****************')
myList = ['Thoughts', 'become', 'things.']
newList = myList
newList[-1] = 'actions.'
print(newList)
print(myList)

print('***************deep copy*****************')
myList = ['Thoughts', 'become', 'things.']
newList = myList[:]
newList[-1] = 'actions.'
print(newList)
print(myList)

# 리스트 내포
print('***************리스트 내포*****************')
nums = [1, 2, 3, 4, 5]
squares = []
for x in nums:
    squares.append(x ** 2)

print(squares)

print('***************리스트 내포*****************')
nums = [1, 2, 3, 4, 5]
squares = [x ** 2 for x in nums]
print(squares)

print('***************리스트 내포*****************')
nums = [1, 2, 3, 4, 5]
even_squares = [x ** 2 for x in nums if x % 2 == 0]
print(even_squares)

# 2.4.2 변경이 불가능한 튜플
print('***************튜플은 다른 리스트나 내장함수도 원소로 가질 수 있음*****************')
myTuple = ('a', 'b', 'c', [10, 20, 30], abs, max)

print('***************인덱싱을 사용하여 4번째 원소인 리스트를 출력*****************')
print(myTuple[3])

print('***************5번째 원소인 내장함수 abs()에 -100을 파라미터로 전달*****************')
print(myTuple[4](-100))

print('***************6번째 원소인 내장함수 max()에 리스트를 파리미터로 전달*****************')
print(myTuple[5](myTuple[3]))

# 2.4.3 {키:값} 형태 딕셔너리
print('***************{키:값} 형태 딕셔너리*****************')
crispr = {'EDIT':"Editas Medicine", 'NTLA':'Intellia Threpeutics'}
print(crispr['EDIT'])

print('***************{키:값} 형태 딕셔너리 - 원소 추가*****************')
crispr['CRSP'] = 'CRISPR Therapeutics'
print(crispr)
print(len(crispr))

# 2.4.4 문자열 포맷 출력
print('***************2.4.4 문자열 포맷 출력*****************')

print('***************2.4.4 문자열 포맷 출력 - % 기호 방식*****************')
for x in crispr:
    print('%s : %s' % (x, crispr[x]))

print('***************2.4.4 문자열 포맷 출력 - {} 기호 방식*****************')
for x in crispr:
    print('{} : {}'.format(x, crispr[x]))

print('***************2.4.4 문자열 포맷 출력 - f-strings 방식*****************')
for x in crispr:
    print(f'{x}:{crispr[x]}')

# 2.4.5 중복 없는 셋 (set)
# set - 중복이 없는 원소 집합
print('***************2.4.5 중복 없는 셋 (set)*****************')
s = {'A','P','P','L','E'}
print(s)

print('***************2.4.5 중복 없는 셋 (set) - 생성한 순서대로 원소가 저장되지는 않음*****************')
mySet = {'B', 6, 1, 2}
print(mySet) # 개판이네..

print('***************2.4.5 중복 없는 셋 (set) - 셋 내부에 특정 원소가 존재하는지 검사*****************')
if 'B' in mySet:
    print("'B' exists in", mySet)

print('***************2.4.5 중복 없는 셋 (set) - 셋은 인덱싱 불가한 대신 원소들의 교,합,차 집합을 구할 수 있다.*****************')
setA = {1,2,3,4,5}
setB = {3,4,5,6,7}

print(setA.intersection(setB))
print(setA & setB)

print(setA.union(setB))
print(setA | setB)

print(setA.difference(setB))
print(setA-setB)

print(setB.difference(setA))
print(setB-setA)

print('***************2.4.5 중복 없는 셋 (set) - 빈 셋은 s=set() 으로 생성해야 한다*****************')
s = set()
print(s)

print('***************2.4.5 중복 없는 셋 (set) - 셋을 활용하면 리스트에서 중복 원소를 간단히 제거할 수 있다*****************')
ls = [1,3,5,2,2,3,4,2,1,1,1,5]
print(list(set(ls)))

# 2.4.6 타임잇으로 성능 측정하기
print('***************2.4.6 타임잇으로 성능 측정하기*****************')

print('***************2.4.6 타임잇으로 성능 측정하기 - 순회 속도 비교*****************')
import timeit

iteration_test = """
for i in itr:
    pass
"""

print(timeit.timeit(iteration_test, setup='itr = list(range(10000))', number=1000))
print(timeit.timeit(iteration_test, setup='itr = tuple(range(10000))', number=1000))
print(timeit.timeit(iteration_test, setup='itr = set(range(10000))', number=1000))

print('***************2.4.6 타임잇으로 성능 측정하기 - 검색 속도 비교*****************')
search_test = """
import random
x = random.randint(0, len(itr)-1)
if x in itr :
    pass
"""

print(timeit.timeit(search_test, setup='itr = list(range(10000))', number=1000))
print(timeit.timeit(search_test, setup='itr = tuple(range(10000))', number=1000))
print(timeit.timeit(search_test, setup='itr = set(range(10000))', number=1000))

# 2.5 변수와 함수
print('***************2.5 변수와 함수*****************')
# 2.5.1 변수
print('***************2.5.1 변수*****************')

print('***************2.5.1 변수 - 정수형*****************')
i = 3
print(i)
print(type(i))

print('***************2.5.1 변수 - 실수형*****************')
f = 1.0
print(f)
print(type(f))

print('***************2.5.1 변수 - 정수형과 실수형의 계산 결과는 실수형으로 처리*****************')
var = i * f
print('{}:{}'.format(var, type(var)))

print('***************2.5.1 변수 - 제한 없는 정수형*****************')
googol = 10 ** 100 # pow(10,100)
print(type(googol))
print(googol)

print('***************2.5.1 변수 - dir() 함수*****************')
s = 'string' # 문자열
print(type(s))
print(dir(s))

print('***************2.5.1 변수 - 예약어*****************')
# 변수명으로 사용할 수 없는 단어
help('keyword')

# 2.5.2 함수
print('***************2.5.2 함수*****************')

print('***************2.5.2 함수 - 연평균 성장률 (CAGR) 구하기*****************')
def getCAGR(first, last, years):
    return (last/first)**(1/years)-1

# 삼성 전자는 1998년 4월 27일 65300원이던 주가가 액면 분할 직전인 2018년 4월 27일 2669000원이 되기까지 20년간 4087% 로 상승함. 이 기간 연 평균 성장률은 20.38%
cagr = getCAGR(65300,2669000,20)
print("SEC CACR: {: .2%}".format(cagr))

print('***************2.5.2 함수 - None 반환값*****************')
def fun1():
    pass

def fun2():
    return

def fun3():
    return None

print(fun1()); print(fun2()); print(fun3());

print(type(None))

print(fun1()==None)
print(fun1() is None)

print('***************2.5.2 함수 - 여러 결괏값 반환*****************')
def myFunc():
    var1 = 'a'
    var2 = [1,2,3]
    var3 = max
    return var1, var2, var3 # 여러 개의 결괏값은 기본적으로 튜플 타입으로 반환된다.

print(myFunc())

print('***************2.5.2 함수 - 여러 결괏값 반환 - 함수에서 반환한 순서대로 여러 객체로 나누어 받기*****************')
s, l, f = myFunc()
print(s)
print(type(s))
print(l)
print(type(l))
print(f)
print(type(f))

print('***************2.5.2 함수 - 람다*****************')
# 람다는 이름 없는 함수를 만들 때 사용
insertComma = lambda x : format(x, ',')
print(insertComma(1234567889))

print('***************2.5.2 함수 - 내장 함수 리스트*****************')
abs = 1
print(abs)
print(abs(-100))


# TODO: - p51























