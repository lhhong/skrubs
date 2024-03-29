#!/usr/bin/python

from tetromino import Tetromino

class Field():

    WIDTH = 10
    HEIGHT = 20

    def __init__(self, state=None):
        if state:
            self.state = state
        else:
            self.state = [[' ' for cols in range(Field.WIDTH)]
                          for rows in range(Field.HEIGHT)]
        self.cleared = 0

    def __str__(self):
        BAR = '   ' + '-' * (Field.WIDTH * 2 + 1) + '\n    ' + \
            ' '.join(map(str, range(Field.WIDTH))) + '\n'
        return BAR + '\n'.join([
            '{:2d} |'.format(i) + ' '.join(row) + '|'
                for i, row in enumerate(self.state)]) + '\n' + BAR

    def _test_tetromino(self, tetromino, row, column):
        """
        Tests to see if a tetromino can be placed at the specified row and
        column. It performs the test with the bottom left corner of the
        tetromino at the specified row and column.
        """
        assert column >= 0
        assert column + tetromino.width() <= Field.WIDTH
        assert row - tetromino.height() + 1 >= 0
        assert row < Field.HEIGHT
        for ti, si in list(enumerate(range(row - tetromino.height() + 1,
                                           row + 1)))[::-1]:
            for tj, sj in enumerate(range(column, column + tetromino.width())):
                if tetromino[ti][tj] != ' ' and self.state[si][sj] != ' ':
                    return False
        return True

    def _place_tetromino(self, tetromino, row, column):
        """
        Place a tetromino at the specified row and column.
        The bottom left corner of the tetromino will be placed at the specified
        row and column. This function does not perform checks and will overwrite
        filled spaces in the field.
        """
        assert column >= 0
        assert column + tetromino.width() <= Field.WIDTH
        assert row - tetromino.height() + 1 >= 0
        assert row < Field.HEIGHT
        for ti, si in list(enumerate(range(row - tetromino.height() + 1,
                                           row + 1)))[::-1]:
            for tj, sj in enumerate(range(column, column + tetromino.width())):
                if tetromino[ti][tj] != ' ':
                    self.state[si][sj] = tetromino[ti][tj]

    def _get_tetromino_drop_row(self, tetromino, column):
        """
        Given a tetromino and a column, return the row that the tetromino
        would end up in if it were dropped in that column.
        Assumes the leftmost column of the tetromino will be aligned with the
        specified column.
        """
        assert isinstance(tetromino, Tetromino)
        assert column >= 0
        assert column + tetromino.width() <= Field.WIDTH
        last_fit = -1
        for row in range(tetromino.height(), Field.HEIGHT):
            if self._test_tetromino(tetromino, row, column):
                last_fit = row
            else:
                return last_fit
        return last_fit

    def _line_clear(self):
        """
        Checks and removes all filled lines.
        """
        lines = 0
        for row in self.state:
            # if (row.count(' ') == 0):
            #     print(row, row.count(' '))
            if row.count(' ') == 0:
                lines += 1
        self.cleared = lines
        self.state = list(filter(lambda row: row.count(' ') != 0, self.state))
        while len(self.state) < Field.HEIGHT:
            self.state.insert(0, [' ' for col in range(Field.WIDTH)])

    def copy(self):
        """
        Returns a shallow copy of the field.
        """
        return Field([row[:] for row in self.state])

    def drop(self, tetromino, column):
        """
        Drops a tetromino in the specified column.
        The leftmost column of the tetromino will be aligned with the specified
        column.
        Returns the row it was dropped in for computations.
        """
        assert isinstance(tetromino, Tetromino)
        assert column >= 0
        assert column + tetromino.width() <= Field.WIDTH
        row = self._get_tetromino_drop_row(tetromino, column)
        assert row != -1
        self._place_tetromino(tetromino, row, column)
        self._line_clear()
        return row

    def count_gaps(self):
        """
        Check each column one by one to make sure there are no gaps in the
        column.
        """
        return sum(
            ["".join([row[col] for row in self.state]).lstrip().count(' ')
             for col in range(Field.WIDTH)])

    def height(self):
        """
        Returns the height on the field of the highest placed tetromino on the
        field.
        """
        for i, row in enumerate(self.state):
            if ''.join(row).strip():
                return Field.HEIGHT - i
        return 0

    def lines_cleared_points(self):
        if self.cleared < 2:
            return self.cleared
        if self.cleared == 2:
            return 3
        if self.cleared == 3:
            return 5
        if self.cleared == 4:
            return 8
        return 0

    def bumpiness(self):
        col = 0
        diff = []
        for col in range(self.WIDTH):
            column = [row[col] for row in self.state]
            i =0
            # print(column)
            while column[i] == ' ' and i < 19:
                i+=1
            if col == 0:
                height = i
            else:
                diff.append(abs(i-height))
                height = i
                # print(height, column[i])
        return sum(diff)

def evaluate(seq) :
    import sys
    f = Field()
    from optimizer import Optimizer
    answer = []
    for i in range(len(seq)):
        t = Tetromino.create(seq[i])
        try:
            opt = Optimizer.get_optimal_drop(f, t)
            t.rotate(opt['tetromino_rotation'])
            f.drop(t, opt['tetromino_column'])
        except:
            opt = {"tetromino_rotation":0,"tetromino_column":0}
        action = int(str(opt['tetromino_rotation'])+str(opt['tetromino_column']))
        answer.append(action)
        # print(f, t, i, action)
    return answer
        # i = input()
    # t = Tetromino.JTetromino().rotate_right()
    # print(t)
    # f.drop(t, 0)
    # print(f)
    # f.drop(Tetromino.LTetromino(), 2)
    # print(f)
    # f.drop(Tetromino.JTetromino().rotate_left(), 5)
    # print(f)
    # t = Tetromino.LTetromino().flip()
    # f.drop(t, 0)
    # f.drop(Tetromino.TTetromino().flip(), 0)
    # f.drop(Tetromino.JTetromino(), 4)
    # print(f)
