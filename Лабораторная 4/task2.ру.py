def get_count_char(str_):
    dict = {}
    str_ = "".join(str_.split())
    str_ = str_.lower()
    for word in str_:
        if word.isalpha():
            if word in dict:
                dict[word] += 1
            else:
                dict[word] = 1
    return dict

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
dict = get_count_char(main_str)
print(get_count_char(main_str))
