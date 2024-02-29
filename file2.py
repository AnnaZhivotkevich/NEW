#конь
class Knight(object):
    def __init__(self, color):
        self.color = color

    def check_move(self, board, x, y):
        x_x1 = Board.po_x[x[0]] #первая координата
        x_y1 = int(Board.po_y[x[1]])
        y_x2 = Board.po_x[y[0]] #новая координата
        y_y2 = int(Board.po_y[y[1]])
        #для хода: буквой Г(2 клетки по верт + 1 по горизонт или 2 по горизонтали + 1 по вертикали)
        if ((abs(x_x1 - y_x2) == 1 and abs(x_y1 - y_y2) == 2) or (abs(x_x1 - y_x2) == 2 and (x_y1 - y_y2) == 1)) and (board.get_color(y) != board.get_color(x)):
            return True
        else:
            return False

    def __repr__(self):  #вывод фигур коня
        return (' ♘', ' ♞')[self.color]
