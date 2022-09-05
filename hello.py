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
print(word[0]+word[1]+word[2]+word[3]+word[4]+word[5])

print(word[-6])
print(word[-6]+word[-5]+word[-4]+word[-3]+word[-2]+word[-1])

# 슬라이싱
print('***************슬라이싱*****************')
print(word[:3])
print(word[3:])

# 2.3.2 산술 연산
print('***************산술 연산*****************')
print(1+2)
print(3-5)
print(5*8)
print(2**8)
print(pow(2,8))
print(5/3)
print(5//3) # 몫
print(5%3) # 나머지

x=2
x +=2
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

FAANG = ['FB','AMZN','AAPL','NFLX','GOOGL']
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
while i >=0:
    i +=1
    if(i%2)==0:
        continue
    if i> 5:
        break
    print(i)
else:
    print('Condition is False.')


# try except 예외 처리
print('***************try except 예외 처리*****************')
try:
    1/0
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

L=[[1,2], [3,4]]
print(L[0], L[1])

print(L[0][1])
print(L[1][1])

print(L+L)
print(L*3)

# split() 함수
print('***************split() 함수*****************')
myList = 'Thoughts become things.'.split()
print(type(myList))
print(myList)

# join() 함수
print('***************join() 함수*****************')
print(' '.join(myList))


# append() 와 extend()
print('***************append() 함수*****************') # 넘겨 받은 인수의 자료형에 상관 없이 리스트 뒤에 그대로 추가
L = [1,2]
L.append([3,4])
print(L)
L.append(5)
print(L)

print('***************extend() 함수*****************') # 넘겨받은 인수가 반복 자료형일 경우, 반복 자료형 내부의 각 원소를 추가
L = [3,2]
print(L)
L.extend([3,4])
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
print('2012/01/04'.replace('/','-'))

# 천 단위 숫자를 쉼표로 구분하기
print('***************천 단위 숫자를 쉼표로 구분하기*****************')
print('1,234,567,890'.split(','))
print(''.join('1,234,567,890'.split(',')))
print('1,234,567,890'.replace(',',''))

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