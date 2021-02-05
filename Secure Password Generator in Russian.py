from random import *

def generate_password(the_length_of_a_password, chars):
    password = []
    for _ in range(the_length_of_a_password):
        password.append(choice(chars))
    shuffle(password)
    password = ''.join(password)
    return password

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
exceptions = 'il1Lo0O'
chars = ''
again = input('Если Вам необходимо сгенерировать пароль/и - введите "да", если хотите выйти введите - "нет": ')

while again == 'y' or again == 'yes' or again == 'yep' or again == 'да' or again == 'д' or again == 'ага' or again == 'угу' or again == 'ад' or again == 'lf' or again == 'l':
    print('Отлично!')
    print('К созданию пароля необходимо подойти ответственно, вне зависимости от вида и важности ресурса, где он будет использоваться. При создании сложного пароля стоит придерживаться следующих правил: \n'
          '- Пароль должен содержать не менее 8 символов, а лучше – 10 и более. \n'
          '- Наличие цифр и букв верхнего и нижнего регистров. \n'
          '- Наличие специальных знаков – «@», «$», «&» и т.д. (если допустимо их присутствие).')
    print()

    chars = ''
    number_of_passwords = int(input('Сколько паролей необходимо сгененрировать? Введите число: '))
    the_length_of_a_password = int(input('Какой длины должен быть пароль? Введите требуемое количество символов: '))
    numbers_in_the_password = input('Должен ли пароль содержать цифры (0123...)? Введите - "да" если нужны и "нет", если цифры не требуются: ').strip()
    uppercase_in_the_password = input('Должен ли пароль содержать прописные буквы (ABCD...)? Введите - "да" если нужны и "нет", если прописные буквы не требуются: ').strip()
    lowercase_in_the_password = input('Должен ли пароль содержать строчные буквы (abcd...)? Введите - "да" если нужны и "нет", если строчные буквы не требуются: ').strip()
    punctuation_in_the_password = input('Должен ли пароль содержать символы пунктуации (!#$%&*+-=?@^_)? Введите - "да" если нужны и "нет", если символы пунктуации не требуются: ').strip()
    exceptions_in_the_password = input('Исключать ли неоднозначные символы (il1Lo0O) в пароле? Введите - "да" если Вы хотите исключить из пароля эти символы, и "нет", если неоднозначные символы нужно добавить в пароль: ').strip()
    print()

    if numbers_in_the_password == 'да' or numbers_in_the_password == 'д' or numbers_in_the_password == 'ага' or numbers_in_the_password == 'угу' or numbers_in_the_password == 'ад' or numbers_in_the_password == 'lf' or numbers_in_the_password == 'y' or numbers_in_the_password == 'l':
        chars += digits
    if lowercase_in_the_password == 'да' or lowercase_in_the_password == 'д' or lowercase_in_the_password == 'ага' or lowercase_in_the_password == 'угу' or lowercase_in_the_password == 'ад' or lowercase_in_the_password == 'lf' or lowercase_in_the_password == 'y' or lowercase_in_the_password == 'l':
        chars += lowercase_letters
    if uppercase_in_the_password == 'да' or uppercase_in_the_password == 'д' or uppercase_in_the_password == 'ага' or uppercase_in_the_password == 'угу' or uppercase_in_the_password == 'ад' or uppercase_in_the_password == 'lf' or uppercase_in_the_password == 'y' or uppercase_in_the_password == 'l':
        chars += uppercase_letters
    if punctuation_in_the_password == 'да' or punctuation_in_the_password == 'д' or punctuation_in_the_password == 'ага' or punctuation_in_the_password == 'угу' or punctuation_in_the_password == 'ад' or punctuation_in_the_password == 'lf' or punctuation_in_the_password == 'y' or punctuation_in_the_password == 'l':
        chars += punctuation
    if exceptions_in_the_password == 'нет' or exceptions_in_the_password == 'н' or exceptions_in_the_password == 'неа' or exceptions_in_the_password == 'не' or exceptions_in_the_password == 'ен' or exceptions_in_the_password == 'no' or exceptions_in_the_password == 'n' or exceptions_in_the_password == 'yt' or exceptions_in_the_password == 'ytn':
        chars += exceptions
    if exceptions_in_the_password == 'да' or exceptions_in_the_password == 'д' or exceptions_in_the_password == 'ага' or exceptions_in_the_password == 'угу' or exceptions_in_the_password == 'ад' or exceptions_in_the_password == 'lf' or exceptions_in_the_password == 'y' or exceptions_in_the_password == 'l':
        for c in chars:
            if c == 'i' or c == 'l' or c == '1' or c == 'L' or c == 'o' or c == '0' or c == 'O':
                chars = chars.replace(c, '')

    passwords = []

    for _ in range(number_of_passwords):
        passwords.append(generate_password(the_length_of_a_password, chars))

    print(*passwords, sep='\n')
    print()
    again = input('Если Вам необходимо сгенерировать пароль/и - введите "да", если хотите выйти введите - "нет": ')
else:
    print('Возвращайтесь, если понадобится генерация надёжного пароля!')
    exit()





