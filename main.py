"""
Описание:
Этот бот был написан за 2 дня в ходе пиксельной войны на сайте replace.live
на бабушкином компьютере когда мне было 14 лет.

Я даже не знаю как вам описать для чего этот бот, вот есть на сайте холст, допустим 1024*1024 пикселя
и ты можешь раз в Н-ное количество времени закрасить пиксель на нём, вот этот бот как раз для таких битв
этот бот и создан

Хоть бот и сделан для джема, но позже я сделал его более настраиваемым,
с этими настройками он может рисовать даже в Paint

Как использовать:
1. Изменить настройки под себя
2. Запустить программу
3. Следовать инструкциям в логе
4. Развлекатся )))
Выйти можно если зажать Esc
"""

import pyautogui
import keyboard
import time

# ------------------ПОЛЬЗОВАТЕЛЬСКИЕ ПАРАМЕТРЫ----------------------
WAIT_TIME = 1  # количество времени (сек) в течении которых нельзя ничего изменять

OFSET_IMAGE_AGAIN = (10, 0)  # офсет следующего изображения (0, 0) - будет печатать на предыдущем

PRESS_ON_CHOOSE_PIXEL = False  # Если False, то бот не будет нажимать когда нужно только выбрать клетку
RELATIVE_MOVE = True  # Если True, то движение будет не от центра экрана, а относительно предыдущей позиции
# (при выборе клетки она передвигается в центр)

# Если True, то при выборе цвета он его считает
# и не будет закрашивать клетку если она уже нужного цвета
# (если кнопка цвета будет другого цвета, то эта опция не будет работать правильно)
# False, чтобы выключить
COLOR_CHECK_MATCHES = True

# Массив нужных действий в виде:
# (поменять_клеток_по_горизонали, поменять_клеток_по_вертикали, *необязательно*поменять_цвет_из_палитры_на),

# С такой справкой будет удобнее)
# " " - ничего
# "0" - белый
# "1" - серый
# "2" - чёрный
# "3" - красный
# "4" - оранжевый
# "5" - жёлтый
# "6" - зелёный
# "7" - синий
# "8" - коричневый
# "9" - розовый

'''
USING_COLORS = 6 # Количество цветов: максимальный +1 (нулевой)
PICTURE_DROWING = [ # Челик
"      222   ",
"   22222222 ",
"222222222222",
" 4444444444 ",
" 4 4 ",
" 4 15 51 4 ",
" 4 4 ",
" 4 3 3 4 ",
" 4 333333 4 ",
" 4 4 ",
" 4444444444 "
]'''

# " " - ничего
# "0" - белый
# "1" - чёрный
# "2" - голубой
# "3" - бирюзовый
# "4" - фиолетовый
'''
USING_COLORS = 5 # Количество цветов: максимальный +1 (нулевой)
PICTURE_DROWING = [ # IMAGINATION team
"222222 22  22  222   222  22222 2   2  222  22222 22222  222  2   2",
"  22   222222 2   2 2   2   2   22  2 2   2   2     2   2   2 22  2",
"  33   3 33 3 3   3 3       3   3 3 3 3   3   3     3   3   3 3 3 3",
"  33   3    3 33333 3  33   3   3 333 33333   3     3   3   3 3 333  333 33  3  2 2",
"  44   4    4 4   4 4   4   4   4  44 4   4   4     4   4   4 4  44   3  32 323 343",
"444444 4    4 4   4  444  44444 4   4 4   4   4   44444  444  4   4   3  33 3 3 3 3"
]'''

# " " - ничего
# "0" - белый
# "1" - чёрный
# "2" - фон (жёлтый)
# "3" - зелень светлая
# "4" - зелень тёмная
# "5" - коричневый
# "6" - кожный
# "7" - тёмнокожный
USING_COLORS = 8  # Количество цветов: максимальный +1 (нулевой)
PICTURE_DROWING = [  # Монолиза
    "22222222222222222222222222",
    "22222222222211111222222222",
    "22222222222155111122222222",
    "22222222221666611111222222",
    "42222222221666661111222222",
    "44222222216666667111122222",
    "44222222216766767111122224",
    "44333442216566567111122324",
    "43333333416676667111123344",
    "43333333316676667111133334",
    "33333333316677667111133333",
    "33333333311666667111133333",
    "34333333311166671111133343",
    "34333333311117111111134444",
    "34334443331117777111114444",
    "43344444441176666555514444",
    "44344444411666666655111444",
    "43334444117666666751155144",
    "43333444117666666755555144",
    "43333441176666667555111111",
    "44333411176676667555111111",
    "33333311177766677111111111",
    "43333111111777711111111551",
    "44333111111111111111555111",
    "44441111111111111155551111",
    "44411111111111111155111111",
    "44111111111111111441111111"
]
# -----------------------------------------------------------------

# -------------------КАЛИБРОВОЧНЫЕ ПЕРЕМЕННЫЕ----------------------
# можете заменить это значения если знаете конкретное число (они выводятся в лог, 0 - калибровать)
TRANS_PIXELS = 0  # Смещение между соседними пикселями (0 - калибровка)

MID_POS = (0, 0)  # координаты центра (-1 середина, 0 - калибровка)
CONFIRM_COLOR_POS = (-1, -1)  # координаты кнопки подтверждения выбора цвета
CONFIRM_PAINT_POS = (-1, -1)  # координаты кнопки подтверждения окраски

# позиции цветов палитре в виде: [(1245, 214), (1243, 1354), (1458, 2463), (254б, 3544)]
# должно совпадать с COLOR_COUNT, иначе начнётся калибровка
COLORS_INFO = []


# -----------------------------------------------------------------


# -----------------------------ФУНКЦИИ-----------------------------
def draw_mark():  # функция для рисования курсором мыши галочку
    pyautogui.moveRel(-15, -15, duration=0.1)
    pyautogui.moveRel(15, 15, duration=0.1)
    pyautogui.moveRel(15, -20, duration=0.1)
    pyautogui.moveRel(-15, 20, duration=0.1)


# -----------------------------------------------------------------


# ----------------------------КАЛИБРОВКА----------------------------
xSize, ySize = pyautogui.size()
print("Разрешение экрана - " + str(xSize) + ":" + str(ySize))

if MID_POS[0] == -1 == MID_POS[1]:
    MID_POS = int(xSize / 2), int(ySize / 2)
elif MID_POS[0] == 0 == MID_POS[1]:
    print("В течении 8 секунд наведите курсор в начало (центр)")
    time.sleep(8)

    MID_POS = [pyautogui.position().x, pyautogui.position().y]
    print("Центр - " + str(MID_POS))

    pyautogui.moveTo(MID_POS[0], MID_POS[1], duration=0.4)

if TRANS_PIXELS == 0:  # опреляем смещение между соседними пикселями если не указано
    print("В течении 8 секунд наведите курсор в центр пикселя находящийся на 1 ниже чем центральный")
    time.sleep(8)

    _, TRANS_PIXELS = pyautogui.position()
    TRANS_PIXELS = TRANS_PIXELS - MID_POS[1]

    print("Смещение между соседними пикселями - " + str(TRANS_PIXELS) + "\n")
    draw_mark()

if CONFIRM_COLOR_POS[0] == 0 == CONFIRM_COLOR_POS[1]:
    print("В течении 5 секунд наведите курсор на кнопку подтверждения окраски")
    time.sleep(5)

    draw_mark()
    CONFIRM_COLOR_POS = pyautogui.position()
    print("Координаты кнопки подтверждения выбора цвета - " + str(CONFIRM_COLOR_POS))

if CONFIRM_PAINT_POS[0] == 0 == CONFIRM_PAINT_POS[1]:
    print("В течении 5 секунд наведите курсор на кнопку подтверждения окраски")
    time.sleep(5)

    draw_mark()
    CONFIRM_PAINT_POS = pyautogui.position()
    print("Координаты кнопки подтверждения окраски - " + str(CONFIRM_PAINT_POS))

if len(COLORS_INFO) != USING_COLORS:
    COLORS_INFO = []
    for i in range(USING_COLORS):
        print(F"В течении 4 секунд наведите курсор на {i + 1} цвет из палитры")
        time.sleep(4)

        COLORS_INFO.append(pyautogui.position())
        draw_mark()

    print("Позиции цветов: " + str(COLORS_INFO))
# -----------------------------------------------------------------

# ---------------------ОСНОВНАЯ ПРОГРАММА---------------------
executed_now_x = -1
executed_now_y = 0
last_point = MID_POS
color_last = " "
color_now_rgb = (0, 0, 0)

pyautogui.FAILSAFE = False

while not keyboard.is_pressed("Esc"):  # выполняем пока не будет нажата Esc
    # переход на следующее действие
    executed_now_x += 1

    if executed_now_x >= len(PICTURE_DROWING[executed_now_y]):  # если действия кончились, то давайте заного
        executed_now_x = 0
        executed_now_y += 1

        # Переводим курсор на следующую строку
        last_point[0] -= (len(PICTURE_DROWING[executed_now_y - 1]) - 1) * TRANS_PIXELS
        last_point[1] += TRANS_PIXELS

        if executed_now_y >= len(PICTURE_DROWING):  # если действия закончились, то давайте заного
            last_point[1] -= len(PICTURE_DROWING) * TRANS_PIXELS

            last_point[0] += OFSET_IMAGE_AGAIN[0] * TRANS_PIXELS
            last_point[1] += OFSET_IMAGE_AGAIN[1] * TRANS_PIXELS

    executed_now_y = 0

    # Получаем текущее действие
    exec_color = PICTURE_DROWING[executed_now_y][executed_now_x]
    # Давайте немного расскажем о себе в консоль
    print(F"Цвет: " + ("не задан, пропускаем клетку" if exec_color == " " else F"{exec_color}"))

    # Если цвет отличается
    if color_last != exec_color and exec_color != " ":
        # Теперь-то мы его юзали, запомним это
        color_last = exec_color

        # Нажимаем нужный нам цвет
        pyautogui.moveTo(COLORS_INFO[int(exec_color)][0], COLORS_INFO[int(exec_color)][1])
        pyautogui.click()
        # берём цвет
        color_now_rgb = pyautogui.screenshot().getpixel(COLORS_INFO[int(exec_color)])

    if CONFIRM_COLOR_POS[0] != -1:  # Если надо, нажимаем на кнопку подтверждения цвета
        pyautogui.moveTo(CONFIRM_COLOR_POS[0], CONFIRM_COLOR_POS[1])
        pyautogui.click()

    # Идём в предыдущую точку
    if RELATIVE_MOVE:
        pyautogui.moveTo(last_point[0], last_point[1])  # Относительное движение
    else:
        pyautogui.moveTo(last_point[0], last_point[1])
        pyautogui.click()
        pyautogui.moveTo(MID_POS[0], MID_POS[1])  # Движение от центра

    if PRESS_ON_CHOOSE_PIXEL:  # не надо её раскрашивать если она не просто выбирается
        pyautogui.click()

    # Перемещаем мышку на указанное в массиве количество клеток
    pyautogui.moveRel(TRANS_PIXELS, 0)

    if RELATIVE_MOVE:  # берём координаты чтоб потом вернуть мышку назад
        last_point = [pyautogui.position().x, pyautogui.position().y]
    else:
        pyautogui.moveTo(MID_POS[0], MID_POS[1])  # или же обратно к центру, ессли движение от центра

    if exec_color == " ":  # если нам ничего не надо делать, то просто пропускаем итерацию
        continue

    # Если разрешено проверять цвет, то делаем это
    if COLOR_CHECK_MATCHES:
        pixColor = pyautogui.screenshot().getpixel(MID_POS if RELATIVE_MOVE else last_point)  # берём цвет пикселя
        if pixColor == color_now_rgb:  # всё и так норм, пропускаем мут
            continue
        else:  # наконец-то кликаем и разукрашиваем пиксель
            pyautogui.click()
            # И подтверждаем окраску если об этом указанно
            if CONFIRM_PAINT_POS[0] != -1:
                pyautogui.moveTo(CONFIRM_PAINT_POS[0], CONFIRM_PAINT_POS[1])
                pyautogui.click()

    # ждём прохода мута
    time.sleep(WAIT_TIME)

    print("Выход из программы, спасибо за внимание!")
