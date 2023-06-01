# 2. Класс инициализируется начальными координатами – положением Робота на плоскости,
# обе координаты заключены в пределах от 0 до 100. Робот может передвигаться на одну клетку вверх
# (N), вниз (S), вправо (E), влево (W). Выйти за границы плоскости Робот не может.
# Метод move() принимает строку – последовательность команд перемещения робота,
# каждая буква строки соответствует перемещению на единичный интервал в направлении,
# указанном буквой. Метод возвращает список координат – конечное положение Робота после перемещения.

class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        if x > 100 or x < 0 or y > 100 or y < 0:
            print(f'coordinates must be less than 100 or equal it.\n' \
                           f'also coordinates must be more than 0 or equal it.\n' \
                           f'coordinates used: x = {self.x}, y = {self.y}.')
            raise SystemExit

    def move(self, instruction):
        for step in instruction:
            if step == 'N':
                self.y += 1
            elif step == 'S':
                self.y -= 1
            elif step == 'E':
                self.x += 1
            elif step == 'W':
                self.x -= 1
            else:
                return 'unknown step used.'
        if self.x > 100 or self.x < 0 or self.y > 100 or self.y < 0:
            print('robot exit the plane!')
            raise SystemExit
        else:
            return [self.x, self.y]

kaplan = Robot(55, 5)
print(f'1st try: {kaplan.move("NNSWEEEE")}')
print(f'2nd try: {kaplan.move("asdfEEE")}')

# shepot dalyokih zvezd