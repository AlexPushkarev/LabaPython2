s = input()

length = len(s)
s2 = ''
i = 0
j = 0

for char in s:
    k = 0
    j = 0
    if i < length and s[i] == '_':
        j = i + 1
        s1 = ''
        if s[j] == 'А' or s[j] == 'Б':
            while j < length and s[j] != '_':
                s1 = s1 + s[j]
                j = j + 1
            k = k + 1
    if k != 0:
        for char1 in s1:
            if char1 != ';':
                s2 = s2 + char1
            else:
                print(s2)
                s2 = ''
        print('---------------------------------------')
    i = i + 1