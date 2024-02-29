# ладья
class Rook(object):
    def __init__(self, color):
        self.color = color

    def check_move(self, board, x, y):
        x_x1 = Board.po_x[x[0]]  # первая координата
        x_y1 = int(Board.po_y[x[1]])
        y_x2 = Board.po_x[y[0]]  # новая координата
        y_y2 = int(Board.po_y[y[1]])
        hod_rook = True
        # если ходит по вертикали, то проверяем, есть ли между 2-мя коорд др фигуры (ход вперед)
        if x_x1 == y_x2 and int(x[1]) < int(y[1]) and (board.get_color(y) != board.get_color(x)):
            for i in range(int(x[1]) + 1, int(y[1])):
                y = x[0] + str(i)
                if board.get_color(y) == Empty.color:  # фигур между нет, возможен ход
                    pass
                else:
                    hod_rook = False

        # если ходит по вертикали, то проверяем, есть ли между 2-мя коорд др фигуры (ход назад)
        elif x_x1 == y_x2 and int(x[1]) > int(y[1]) and (board.get_color(y) != board.get_color(x)):
            for i in range(int(x[1]) - 1, int(y[1]), -1):
                y = x[0] + str(i)
                if board.get_color(y) == Empty.color:  # фигур между нет, возможен ход
                    pass
                else:
                    hod_rook = False

        # если ходит по горизонтали, то проверяем, есть ли между 2-мя коорд др фигуры (ход вправа)
        elif x_y1 == y_y2 and ord(y[0]) > ord(x[0]) and (board.get_color(y) != board.get_color(x)):
            for i in range(ord(x[0]) + 1, ord(y[0])):
                y = chr(i) + str(x[1])
                if board.get_color(y) == Empty.color:  # фигур между нет, возможен ход
                    pass
                else:
                    hod_rook = False

        # если ходит по горизонтали, то проверяем, есть ли между 2-мя коорд др фигуры (ход влево)
        elif x_y1 == y_y2 and ord(y[0]) < ord(x[0]) and (board.get_color(y) != board.get_color(x)):
            for i in range(ord(x[0]) - 1, ord(y[0]), -1):
                y = chr(i) + str(x[1])
                if board.get_color(y) == Empty.color:  # фигур между нет, возможен ход
                    pass
                else:
                    hod_rook = False
        else:  # в др случае ход ладьи невозможен
            hod_rook = False
        return hod_rook

    def __repr__(self):  # вывод фигур ладьи
        return (' ♖', ' ♜')[self.color]
