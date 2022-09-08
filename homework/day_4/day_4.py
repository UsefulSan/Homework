import random as r


def mix():
    """Выборирает слово из списка, перемешивает буквы и предлагает пользователю его отгадать"""
    with open('words.txt') as words:
        point = 0
        for word in words:
            word = word.strip().lower()
            word_list = list(word)
            r.shuffle(word_list)
            shuffle_word = ''.join(word_list)
            answer = input(f'Угадайте слово: {shuffle_word}\n').strip().lower()
            if answer == word:
                point += 10
                print(f'Верно! Вы получаете 10 очков.')
            else:
                print(f'Неверно! Верный ответ – {word}.')
        return point


def record_result(user_name, point):
    """запись результата в файл"""
    with open('history.txt', 'a', encoding='utf-8') as record:
        record.write(f'{user_name}: {point}\n')


def print_statistics():
    """Вывод статистики прошлых игр, с учётом этой игры"""
    with open('history.txt') as open_statistics:
        record = 0
        count_game = 0
        for line in open_statistics:
            point = int(line.split()[1])
            if record < point:
                record = point
            count_game += 1
        print(f'Всего игр сыграно: {count_game} \nМаксимальный рекорд: {record}')
        if count_game < 3:
            return False
        return True


def top_3():
    """Выводит топ 3 игроков из файла history.txt"""
    with open('history.txt') as open_statistics:
        list_players = list(map(str.split, open_statistics.readlines()))
        list_players.sort(key=lambda x: (-int(x[1]), x[0]))
        print('Топ 3 игроков: ')
        for i in range(3):
            print(f'{list_players[i][0]} {list_players[i][1]}')


def main():
    user_name = input('Введите ваше имя ')
    score = mix()
    record_result(user_name, score)
    print(f'{user_name}, твой результат {score}')
    flag = print_statistics()
    if flag:
        top_3()


if __name__ == '__main__':
    main()
