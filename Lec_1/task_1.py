# Функция id() возвращает адрес объекта
# в оперативной памяти вашего компьютера
#переменные могут ссылаться на объекты разных типов. И это не вызывает ошибки.
name = "Alex"
age = None

a = 42
print(id(a))
a = "Hello world!"
print(id(a))

#Вывод данных
print(name, age, a, 456, "text", sep= " =/ \= ", end="#")
print("Hello")

#Ввод данных, строчных
#res = input('Введи свой текст: ')
#print('Ты ввел:', res)

#Ввод данных, числовых
#age = int(input('Введи введи свой возраст: ')) #завернули значение input в int

#Осталось до совершеннолетия

ADULT = 21
age = int(input('Введи свой возраст: '))
how_old = ADULT - age
print(how_old, 'Осталось до совершенно летия')