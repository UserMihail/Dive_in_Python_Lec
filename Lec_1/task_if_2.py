# Иначе, else
# Для выполнения кода в случае ложности логического выражения используется
# зарезервированное слово else c обязательным двоеточием после него

pwd = 'text'
res = input('Input password: ')
if res == pwd:
    print('Доступ разрешён')
    print('Но будьте осторожны')
else:
    print('Доступ запрещён')
print('Работа завершена')
