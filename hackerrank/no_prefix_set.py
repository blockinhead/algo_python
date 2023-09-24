# encoding: utf8
# нужно проверить, что в наборе нет слов-префиксов данного слова
# словарь хранит структуру - текущей букве соответствуется словарь со следующими буквами,
# и флаг - является ли данная буква конечной в каком-то уже известном слове
# добавляем буквы по одной, пока не увидим, что данная буква была конечной в каком-то слове,
# или текущая буква является конечной в данном слове, но она при этом есть в словаре
# такая структура - trie


def add_word(d: dict, word: str):
    for i in range(len(word)):
        if word[i] not in d:
            d[word[i]] = {}, i == len(word) - 1
        else:
            if d[word[i]][1] or i == len(word) - 1:
                return False

        d, _ = d[word[i]]

    return True

some_d = {}
print(add_word(some_d, 'abc'))
print(add_word(some_d, 'abc'))
print(add_word(some_d, 'aef'))
print(some_d)
