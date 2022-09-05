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

