print('Добро пожаловать в игру: крестики-нолики!')
# создаем пустое поле, с нумерацией, для удобства играков
field = list(range(1,10))
# оформление, для визуального удобства
def draw_field(field):
    for i in range(3):
        print('|', field[0 + i * 3], '|', field[1 + i * 3], '|', field[2 + i * 3])
# ввод информации от пользователей, проверка правильности ввода
def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input("В какую клеточку поставим " + player_token+"? ")   # подставляем переменную и соединяем в предложение
        try:         #дает обработать ошибку
            player_answer = int(player_answer)
        except:      #выводит что за ошибка, и как исправить
            print("Вы уверены, что ввели номер клетки?")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(field[player_answer-1]) not in "XO"):
                field[player_answer-1] = player_token
                valid = True
            else:
                print("Эта клеточка уже занята")
        else:
            print("Некорректный ввод. Введите число от 1 до 9 чтобы походить.")
# проверка выполнения условия выигрыша,
def check_win(field):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if field[each[0]] == field[each[1]] == field[each[2]]:
            return field[each[0]]
    return False
# создане цикла, для выведения информации, прочтения пользователем
def main(field):
    counter = 0
    win = False
    while not win:
        draw_field(field)   #очередность ввода игроками значений
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:      #условия проверки, для выхода из цикла
            tmp = check_win(field)
            if tmp:
                print(tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print("Ничья!")
            break
    draw_field(field)
main(field)