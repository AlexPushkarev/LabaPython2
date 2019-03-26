s = input()

print('      ФИО', '                  ', 'О студенте')

a1 = s.find('Иванов')
s1 = s[a1:a1+6]
s2 = s[a1+7:a1+11]
a1 = s.find('Иванович')
s3 = s[a1:a1+8]
a1 = s.find('Студент')
s5 = s[a1:a1+15]
a1 = s.find('23')
s6 = s[a1:a1+7]
stroka_1 = s1 + ' ' + s2 + ' ' + s3 + '   ' + s5 + ',' + s6
print(stroka_1)

a1 = s.find('Петров')
s1 = s[a1:a1+6]
a1 = s.find('Семен')
s2 = s[a1:a1+5]
a1 = s.find('Игоревич')
s3 = s[a1:a1+8]
a1 = s.rfind('Студент')
s5 = s[a1:a1+15]
a1 = s.find('22')
s6 = s[a1:a1+7]
stroka_2 = s1 + ' ' + s2 + ' ' + s3 + '  ' + s5 + ',' + s6
print(stroka_2)