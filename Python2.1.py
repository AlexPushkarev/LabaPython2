s = input()

length = len(s)
i = 0
j = 0
s1 = ''
s2 = ''
buk = 'й', 'ц', 'у', 'к', 'е', 'н', 'г', 'ш', 'щ', 'з', 'х',\
      'ъ', 'ф', 'ы', 'в', 'а', 'п', 'р', 'о', 'л', 'д', 'ж', 'э', 'я', 'ч', 'с', 'м', 'и',\
      'т', 'ь', 'б', 'ю'

for char in s:
    k = 0
    j = 0
    if i < length and s[i] in buk:
        j = i
        s1 = ''
        while j < length and s[j] in buk:
            s1 = s1 + s[j]
            j = j + 1
        if s[j - 2] == 'о':
            if s[j - 1] == 'в':
                s2 = s2 + s1
                k = 1
    if k == 1:
        i = j
    if k != 1:
        i = i + 1

print(s2)