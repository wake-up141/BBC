def lvl_1(s: str) -> str:
    """Выбор метода из предложенных, простые действия над строкой"""
    method = str(input("Выберите метод из upper, lower, capitalize: "))
    if method == "upper":
        return s.upper()
    elif method == "lower":
        return s.lower()
    elif method == "capitalize":
        return s.capitalize()
    else:
        return 'Нет такого метода'

def lvl_2(s: str) -> str:
    """Замена первого вхождения в строке, либо поиск первого вхождения, либо поиск количества вхождений"""
    method = str(input("Выберите метод из find, replace, count: "))
    if method == "replace":
        word_before = str(input("Введите слово, которое хотите заменить: "))
        word_after = str(input("Введите слово, на которое хотите заменить предыдущее: "))
        return s.replace(word_before, word_after)
    elif method == "find":
        word = str(input("Введите слово, первое вхождение которого вы хотите найти: "))
        return str(s.find(word))
    elif method == "count":
        word = str(input("Введите слово, количество вхождений которого вы хотите найти: "))
        return str(s.count(word))
    else:
        return 'Нет такого метода'

def lvl_3(s: str) -> str:
    """Разделение и склейка строки по определенным символам (группам символов)"""
    cut = str(input("Введите символ или группу символов, по которым вы хотите разделить строку: "))
    paste = str(input("Введите символ или группу символов, которую хотите вставить между элементами строки: "))
    return paste.join(s.split(cut))

def lvl_4(s: str) -> bool:
    """Проверка на 'формат' строки, например только цифры либо только буквы"""
    method = str(input("Выберите метод из isdigit, isalpha: "))
    if method == "isdigit":
        return s.isdigit()
    elif method == "isalpha":
        return s.isalpha()
    else:
        return 'Нет такого метода'

def lvl_5(s: str) -> str:
    """Переработка текста в читаемый"""
    b = str('')
    for elem in s:
        if elem.isalpha():
            b+=elem
        else:
            b+=' '
    return ' '.join(b.lower().strip().split())


choose_lvl = str(input("Выберите 'уровень' функции: "))
text = str(input("Введите исходный текст: "))

if choose_lvl == "1":
    print(lvl_1(text))
elif choose_lvl == "2":
    print(lvl_2(text))
elif choose_lvl == "3":
    print(lvl_3(text))
elif choose_lvl == "4":
    print(lvl_4(text))
elif choose_lvl == "5":
    print(lvl_5(text))
