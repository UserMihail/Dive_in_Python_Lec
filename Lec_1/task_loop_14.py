# Цикл с нумерацией элементов, функция enumerate()
# позволяет добавить порядковый номер к элементам 
# итерируемой последовательности. Доработаем пример с животными. 
# Будем выводить порядковый номер перед указанием животного

animals = ['cat', 'dog', 'wolf', 'rat', 'dragon']
for i, animal in enumerate(animals, start=1):    #(i-счетчик, animal- список(указано в ед числе) )
    print(i, animal)    