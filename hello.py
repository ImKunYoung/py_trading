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

