def int_func(txt):
    cap_list = list()
    for w in txt:
        cap_list.append(w.capitalize())
    return ' '.join(cap_list)


word = (input('Введите слово ').split())
print(int_func(word))

phrase = (input('Введите фразу ').split())
print(int_func(phrase))
