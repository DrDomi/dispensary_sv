import csv


def dispensary():

    """Функция нужна для определения, нуждается ли данный код МКБ-10 в диспансерном
    наблюдении терапевтом. Другие специальности не включены. Пока что..."""

    icd_input = input('Введите код МКБ-10: ').capitalize()
    icd_split = icd_input[0]
    icd_input = transponding(icd_split) + icd_input[1:]
    print(icd_finder(icd_input))

    with open('icd_list_physician', 'r') as icd:
        icd = icd.read()
        if icd_input in icd:
            print('Подлежит диспансерному наблюдению у терапевта')
        else:
            print('Не подлежит диспансерному наблюдению')


def transponding(letter):

    """Функция переводит русскую букву в соответствующую английскую согласно раскладке qwerty/йцукен"""

    rus = ['Й','Ц','У','К','Е','Н','Г','Ш','Щ','З','Ф','Ы','В','А','П','Р','О','Л','Д','Я','Ч','С','М','И','Т','Ь']
    eng = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
    if letter in rus:
        list_index = rus.index(letter)
        return eng[list_index]
    else:
        return letter


def icd_finder(code):

    """Этот скрипт ищет код МКБ в справочнике и выводит его описание в консоль.
    За csv файл со справочником МКБ благодарен Антону(ak4nv)Кочневу
    Github: https://github.com/ak4nv/mkb10"""

    with open('mkb10.csv', mode='r', encoding='utf-8') as mkb:
        reader = csv.reader(mkb)
        for row in reader:
            if code in row:
                return row[1]
    return 'Указанного кода нет в справочнике МКБ-10'


dispensary()
