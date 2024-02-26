class Piece():
    def __init__(self, letter, colour, pos):
        self.ltr = letter
        self.colour = colour
        self.pos = pos

    def calc_moves(self, piecemoves, flag):
        posblmoves = []
        for trjct in piecemoves:
            x, y = self.pos
            xv = trjct[0]
            yv = trjct[1]
            if flag == "Checker":
                for trjct in piecemoves:
                    x, y = self.pos
                    xv = trjct[0]
                    yv = trjct[1]
                    if 1 <= x + xv <= 8 and 1 <= y + yv <= 8 and b.board[x + xv][y + yv] == ".":
                        posblmoves.append((x + xv, y + yv))
                    elif 1 <= x + xv <= 8 and 1 <= y + yv <= 8 and b.board[x + xv][y + yv] != ".":
                        if b.board[x + xv][y + yv].colour != self.colour:
                            if 1 <= x + xv + xv <= 8 and 1 <= y + yv + yv <= 8 and b.board[x + xv + xv][
                                y + yv + yv] == ".":
                                posblmoves.append((x + xv + xv, y + yv + yv))
                return posblmoves
            if flag == "Pawn":
                if 1 <= x + xv <= 8 and 1 <= y + yv <= 8 and b.board[x + xv][y + yv] == ".":
                    posblmoves.append((x + xv, y + yv))
                if self.firstmv == True and b.board[x + xv + xv][y + yv + yv] == ".":
                    posblmoves.append((x + xv + xv, y + yv + yv))
                for trjct in piecemoves[1:]:
                    xv = trjct[0]
                    yv = trjct[1]
                    if 1 <= x + xv <= 8 and 1 <= y + yv <= 8 and b.board[x + xv][y + yv] != ".":
                        if b.board[x + xv][y + yv].colour != self.colour:
                            posblmoves.append((x + xv, y + yv))
                return posblmoves
            while 1 <= x + xv <= 8 and 1 <= y + yv <= 8:
                if b.board[x + xv][y + yv] != ".":
                    if (b.board[x + xv][y + yv]).colour == self.colour:
                        break
                    elif (b.board[x + xv][y + yv]).colour != self.colour:
                        posblmoves.append((x + xv, y + yv))
                        break
                posblmoves.append((x + xv, y + yv))
                if flag == False:
                    break
                x = x + xv
                y = y + yv
        return posblmoves


class KN(Piece):
    def __init__(self, letter, colour, pos):
        super().__init__(letter, colour, pos)
        self.contmov = True
        self.posmoves = (
        (1, 2), (2, 1), (-1, -2), (-2, -1), (-1, 2), (-2, 1), (1, -2), (2, -1), (0, 1), (1, 0), (0, -1), (-1, 0))


class F(Piece):
    def __init__(self, letter, colour, pos):
        super().__init__(letter, colour, pos)
        self.contmov = False
        self.posmoves = ((3, 1), (3, -1), (-3, 1), (-3, -1), (-2, 0), (-1, 0), (1, 0), (2, 0))


class S(Piece):
    def __init__(self, letter, colour, pos):
        super().__init__(letter, colour, pos)
        self.contmov = False
        self.posmoves = ((2, 2), (2, 1), (2, 0), (2, -1), (2, -2), (-2, 2), (-2, 1), (-2, 0), (-2, -1), (-2, -2))


class C(Piece):
    def __init__(self, letter, colour, pos):
        super().__init__(letter, colour, pos)
        self.contmov = "Checker"
        self.reachedend = False
        if self.colour == "black":
            self.posmoves = ((1, 1), (1, -1))
        else:
            self.posmoves = ((-1, 1), (-1, -1))


class R(Piece):
    def __init__(self, letter, colour, pos):
        super().__init__(letter, colour, pos)
        self.contmov = True
        self.posmoves = ((0, 1), (1, 0), (0, -1), (-1, 0))


class N(Piece):
    def __init__(self, letter, colour, pos):
        super().__init__(letter, colour, pos)
        self.contmov = False
        self.posmoves = ((1, 2), (2, 1), (-1, -2), (-2, -1), (-1, 2), (-2, 1), (1, -2), (2, -1))


class B(Piece):
    def __init__(self, letter, colour, pos):
        super().__init__(letter, colour, pos)
        self.contmov = True
        self.posmoves = ((1, 1), (1, -1), (-1, -1), (-1, 1))


class Q(Piece):
    def __init__(self, letter, colour, pos):
        super().__init__(letter, colour, pos)
        self.contmov = True
        self.posmoves = ((0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1))


class K(Piece):
    def __init__(self, letter, colour, pos):
        super().__init__(letter, colour, pos)
        self.contmov = False
        self.posmoves = ((0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1))


class P(Piece):
    def __init__(self, letter, colour, pos):
        super().__init__(letter, colour, pos)
        self.contmov = "Pawn"
        self.firstmv = True
        if self.colour == "black":
            self.posmoves = ((1, 0), (1, -1), (1, 1))
        else:
            self.posmoves = ((-1, 0), (-1, -1), (-1, 1))


class Board():
    def __init__(self):
        self.win = True
        self.chckrs = False
        self.board = [["  ", "A", "B", "C", "D", "E", "F", "G", "H"],
                      ['8|', 'r', 'n', 'b', 'q', 'k', 'b', 'n', 'r', '|8'], \
                      ['7|', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', '|7']]
        for i in range(2, 6):
            d = []
            d.append(str(8 - i) + "|")
            for j in range(8):
                d.append(".")
            d.append("|" + str(8 - i))
            self.board.append(d)
        for i in range(2, 0, -1):
            d = []
            d.append(str(i) + "|")
            d.extend([el.upper() for el in self.board[i][1:-1]])
            d.append("|" + str(i))
            self.board.append(d)
        self.board.append(self.board[0])
        for i in range(1, 9):
            for j in range(1, 9):
                if self.board[i][j] == ".": continue
                clr = "black" if self.board[i][j].islower() else "white"
                self.board[i][j] = eval(self.board[i][j].upper() + str((self.board[i][j], clr, (i, j))))

    def field(self):
        pr = []
        for row in self.board:
            r = []
            for el in row:
                if type(el) != str:
                    r.append(el.ltr)
                else:
                    r.append(el)
            pr.append(r)
        return pr

    def pr_field(self, clr):
        danger = []
        cn = False
        for r in b.board:
            for el in r:
                if type(el) != str:
                    if el.colour != clr:
                        cn = True
                        danger.extend(el.calc_moves(el.posmoves, el.contmov))
        for r in b.board:
            for el in r:
                if type(el) != str:
                    if el.colour == clr and el.pos in danger:
                        if el.ltr in "Kk":
                            print('\033[36m' + el.ltr + '\033[0m', end=" ")
                        else:
                            print('\033[31m' + el.ltr + '\033[0m', end=" ")
                    else:
                        print(el.ltr, end=" ")
                else:
                    print(el, end=" ")
            print()
        if cn == False:
            b.win = False

    def Checkers(self):
        self.chckrs = True
        for i in range(2, 9, 2):
            b.board[1][i] = C("c", "black", (1,i))
        for i in range(1, 9, 2):
            b.board[2][i] = C("c", "black", (2,i))
        for i in range(2, 9, 2):
            b.board[3][i] = C("c", "black", (3,i))
        for i in range(1, 9, 2):
            b.board[6][i] = C("C", "white", (6,i))
        for i in range(2, 9, 2):
            b.board[7][i] = C("C", "white", (7,i))
        for i in range(1, 9, 2):
            b.board[8][i] = C("C", "white", (8,i))
        for j in [1,3,7]:
            for i in range(1, 9, 2):
                b.board[j][i] = "."
        for j in [2, 6,8]:
            for i in range(2, 9, 2):
                b.board[j][i] = "."
class Player():
    def __init__(self, clr, name):
        self.clr = clr
        if name == "": name = "Игрок"
        self.name = name + "(" + str(clr) + ")"

    def converse(self, pos):
        alph = ["  ", "A", "B", "C", "D", "E", "F", "G", "H"]
        try:
            if len(pos) == 2:
                x, y = pos[1], pos[0]
                if y in alph:
                    y = alph.index(y)
                    x = 8 - int(x) + 1
                    return (x, y)
                else:
                    print("Ошибка ввода")

            else:
                print("Ошибка ввода")
                return False
        except (TypeError, IndexError, ValueError):
            print("Ошибка ввода")

    def move(self, cur, to):
        try:
            x, y = cur
            x1, y1 = to
            fgr = b.board[x][y]
            moves = fgr.calc_moves(fgr.posmoves, fgr.contmov)
            if (x1, y1) in moves:
                if fgr.ltr in ("P", 'p'): fgr.firstmv = False
                fgr.pos = (x1, y1)
                if (fgr.ltr == "C" and x1 == 1) or (fgr.ltr == "c" and x1 == 8):
                    fgr.posmoves = ((-1, 1), (-1, -1), (1, 1), (1, -1))
                if fgr.ltr in "Cc" and abs(x1 - x) != 1:
                    x2 = (x1 + x) // 2
                    y2 = (y1 + y) // 2
                    b.board[x2][y2] = "."
                    b.board[x1][y1] = fgr
                    b.board[x][y] = "."
                    return "eaten"
                b.board[x1][y1] = fgr
                b.board[x][y] = "."
                return True
            else:
                print("Невозможный ход")
                return False
        except (TypeError, IndexError, ValueError):
            print("Ошибка ввода")

    def showmoves(self, pos):
        x, y = pos
        fgr = b.board[x][y]
        d = (b.field()).copy()
        moves = fgr.calc_moves(fgr.posmoves, fgr.contmov)
        for m in moves:
            if d[m[0]][m[1]] != ".":
                d[m[0]][m[1]] = d[m[0]][m[1]] + "*"
            else:
                d[m[0]][m[1]] = "*"
        for row in d:
            for el in row:
                if len(el) != 1:
                    if el[1] == "*":
                        print('\033[32m' + el[0] + '\033[0m', end=" ")
                    else:
                        print(el, end=" ")
                elif el == "*":
                    print('\033[32m' + el + '\033[0m', end=" ")
                else:
                    print(el, end=" ")
            print()

    def checkfrom(self, pos):
        try:
            if self.check(pos):
                x, y = pos
                fgr = b.board[x][y]
                if fgr == ".":
                    print("Выберите клетку с фигуркой")
                    return False
                elif fgr.colour != self.clr:
                    print("Эта фигурка не ваша")
                    return False
                return True
            else:
                return False
        except (TypeError, IndexError, ValueError):
            print("Ошибка ввода")

    def check(self, pos):
        try:
            x1, y1 = pos
            if 1 <= x1 <= 8 and 1 <= y1 <= 8:
                return True
            else:
                print("Введена несуществующая клетка")
                return False
        except (TypeError, IndexError, ValueError):
            print("Ошибка ввода")


global b
b = Board()
c = 1
ch = input("Вы ходите сыграть в шашки? 1 - Да; 2 - Нет: ")
if ch == "1":
    b.Checkers()
pr1 = Player("white", input("Введите своё имя, игрок за белые фигурки:"))
pr2 = Player("black", input("Введите своё имя, игрок за чёрные фигурки:"))
pl = pr1
b.pr_field(pl.clr)
while b.win:
    print("Ход номер:", c, "ход", pl.name)
    k = False
    while k != True:
        cur = input("Введите позицию фигуры, которой будет сделан ход: ")
        cur = pl.converse(cur)
        if cur != False:
            if pl.checkfrom(cur):
                pl.showmoves(cur)
                to = pl.converse(input("Введите позицию для перемещения фигуры: "))
                if pl.check(to):
                    if type(b.board[to[0]][to[1]]) != str:
                        if b.board[to[0]][to[1]].ltr in "Kk":
                            if pl.move(cur, to):
                                b.win = False
                                break
                        if pl.move(cur, to) != False:
                            k = True
                            c += 1
                            pl = [pr1, pr2][(c - 1) % 2]
                    elif pl.move(cur, to):
                        k = True
                        c += 1
                        pl = [pr1, pr2][(c - 1) % 2]
            b.pr_field(pl.clr)
print("Победа игрока", [pr1, pr2][(c - 1) % 2].name)
