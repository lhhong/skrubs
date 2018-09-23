import random
import sys, os
sys.path.append(os.path.abspath('./codeitsuisse/challenges/tetris'))
import field

def evaluate(inputVal):
    seq = inputVal["tetrominoSequence"]
    print(seq)
    actions = field.evaluate(seq)
    return {"actions": actions}

    #
    # board = [[0 for _ in range(20)] for _ in range(10)]
    # surface = [0 for _ in range(10)]
    #
    # def findHoleforO():
    #     prev = 30
    #     candidate = []
    #     for i, s in enumerate(surface):
    #         if s == prev:
    #             candidate.append((prev, i-1))
    #         prev = s
    #     candidate.sort()
    #     if len(candidate) == 0:
    #         return 0
    #     return candidate[0][1]
    #
    # def findMoveForI():
    #
    #     ## TODO find hole to insert vertically first
    #
    #     prev = [30, 30, 30]
    #     candidate = []
    #     for i, s in enumerate(surface):
    #         if s == prev[0] and s == prev[1] and s == prev[2]:
    #             candidate.append((prev, 10 + i-3))
    #         prev[0] = s
    #         prev[1] = prev[0]
    #         prev[2] = prev[1]
    #     candidate.sort()
    #     if len(candidate) == 0:
    #         prev = surface[10]
    #         for i, s in enumerate(reversed(surface)):
    #             candidate.append(((s-prev, i), 10-i))
    #             prev = s
    #         candidate.sort()
    #     return candidate[0][1]
    #
    # def updateBoard(tile, move, surface):
    #
    #     rotation = move // 10
    #     trans = move % 10
    #
    #     if tile == 'J':
    #         pass
    #
    #     if tile == 'O':
    #         for i, t in enumerate(board[trans]):
    #             if t !=0:
    #                 i -= 1
    #                 break
    #         for j, t in enumerate(board[trans + 1]):
    #             if t !=0:
    #                 j -= 1
    #                 break
    #         h = min(j, i)
    #         board[trans+1][h] = 1
    #         board[trans][h] = 1
    #         board[trans+1][h-1] = 1
    #         board[trans][h-1] = 1
    #
    #     if tile == 'I':
    #         if rotation % 2 == 0:
    #             for i, t in enumerate(board[trans]):
    #                 if t !=0:
    #                     i -= 1
    #                     break
    #             for j in range(i-3, i+1):
    #                 board[trans][i] = 1
    #         else:
    #             for i, t in enumerate(board[trans]):
    #                 if t !=0:
    #                     i -= 1
    #                     break
    #             for j, t in enumerate(board[trans + 1]):
    #                 if t !=0:
    #                     j -= 1
    #                     break
    #             for k, t in enumerate(board[trans + 2]):
    #                 if t !=0:
    #                     k -= 1
    #                     break
    #             for l, t in enumerate(board[trans + 3]):
    #                 if t !=0:
    #                     l -= 1
    #                     break
    #             h = min([i, j, k, l])
    #             for t in range(trans, trans+4):
    #                 board[t][h] = 1
    #
    #     for i in range(len(board[0])):
    #         for j in range(len(board)):
    #             if board[j][i] != 1:
    #                 # row not complete
    #                 break
    #         else:
    #             for j in range(len(board)):
    #                 del board[j][i]
    #                 board[j].insert(0, 0)
    #
    #     for i, t in enumerate(board):
    #         for j, t in enumerate(board[i]):
    #             if t !=0:
    #                 break
    #         surface[i] = j
    #
    #     surface = [max(surface) - s for s in surface]
    #
    #     return surface
    #
    # moves = []
    # for i, s in enumerate(seq):
    #     move = None
    #     if s == 'O':
    #         move = findHoleforO()
    #         moves.append(move)
    #
    #     elif s == 'I':
    #         move = findMoveForI()
    #         moves.append(move)
    #
    #     else:
    #         move = random.randint(0,3) * 10 + random.randint(0,9)
    #         moves.append(move)
    #
    #     surface = updateBoard(s, move, surface)
    #
    # return {"actions": moves}


tests = [
    {
        "tetrominoSequence": "IOJLLLTIOOTIOTZSTTTLLIJSZTIT"
    },
    {
        "tetrominoSequence": "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO"
    }
]
