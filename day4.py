MARKED = ['X', 'X', 'X', 'X', 'X']


def read_board():
    brds = []
    with open('resources/day4_input.txt') as f:
        plys = f.readline().strip().split(",")
        line = f.readline()
        while line:
            board = []
            for _ in range(5):
                board.append(f.readline().strip().split())
            brds.append(board)
            line = f.readline()
    return brds, plys


def check_cols(brd):
    for i in range(len(brd)):
        check = []
        for j in range(len(brd)):
            check.append(brd[j][i])
        if check == MARKED:
            return True
    return False


def check_rows(brd):
    for i in range(len(brd)):
        if brd[i] == MARKED:
            return True
    return False


def calculate_score(brd):
    score = 0
    for i in range(len(brd)):
        for j in range(len(brd)):
            if brd[i][j] != 'X':
                score += int(brd[i][j])
    return score


def mark_number(brd, nmbr):
    for i in range(len(brd)):
        for j in range(len(brd)):
            if brd[i][j] == nmbr:
                brd[i][j] = 'X'
    return brd


def play_bingo(brds, plys):
    for ply in plys:
        for brd in brds:
            mark_number(brd, ply)
        for brd in brds:
            if check_rows(brd) or check_cols(brd) is True:
                return calculate_score(brd) * int(ply)


def play_bingo2(brds, plys):
    for ply in plys:
        for brd in brds:
            mark_number(brd, ply)
        for brd in brds:
            if len(brds) > 1:
                if check_rows(brd) or check_cols(brd) is True:
                    brds.remove(brd)
            else:
                return calculate_score(brds[0]) * int(ply)


if __name__ == "__main__":
    boards, plays = read_board()
    print(play_bingo(boards, plays))
    boards, plays = read_board()
    print(play_bingo2(boards, plays))
