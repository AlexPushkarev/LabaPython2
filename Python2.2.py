s = input()

print('     ФИО', end=' ')
print('О студенте'.rjust(45))

list1 = s.split('_')
s1 = ''

count = 0

for i in range(1,  len(list1)):
    count = 0
    list2 = list1[i].split(';')
    for j in list2:
        count = count + 1
        s1 = str(j)
        if count < 4:
            if count == 3:
                if i == 2:
                    print(s1.ljust(24), end='')
                else:
                    print(s1.ljust(25), end='')
            else:
                print(s1, end=' ')
        elif count == 4:
            s1 = str(list2[count])
            print(s1, end=',')
        elif count == 5:
            s1 = str(list2[count-2])
            print(s1)
        s1 = ''


