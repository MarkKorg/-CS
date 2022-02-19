import random

sum = 0
for game in range(1, 101):
    box1 = [False, False, False]
    box2 = [False, False, False]
    box3 = [False, False, False]
    box4 = [False, False, False]
    box5 = [False, False, False]
    box6 = [False, False, False]
    box7 = [False, False, False]
    box8 = [False, False, False]
    box9 = [False, False, False]
    # box[Small ring,Medium ring,Large ring]

    row1 = [box1, box2, box3]
    row2 = [box4, box5, box6]
    row3 = [box7, box8, box9]

    square = [row1, row2, row3]

    '''
    for i in range(0, 3):
        for j in range(0, 3):
            for k in range(0, 3):
                print(square[i][j][k])
    '''

    small = 9
    medium = 9
    large = 9
    # NOT necessary, because square is 3*3


    def checkHorizontal_eq(square):
        win = False
        for row in range(0, 3):
            for ring_size in range(0, 3):
                if square[row][0][ring_size] == square[row][1][ring_size] == square[row][2][ring_size] == True:
                    win = True
        return win


    def checkVertical_eq(square):
        win = False
        for box in range(0, 3):
            for ring_size in range(0, 3):
                if square[0][box][ring_size] == square[1][box][ring_size] == square[2][box][ring_size] == True:
                    win = True
        return win


    def checkDiagonal_eq(square):
        win = False
        for ring_size in range(0, 3):
            if square[2][0][ring_size] == square[1][1][ring_size] == square[0][2][ring_size] == True:
                # Diagonal /
                win = True
            elif square[0][0][ring_size] == square[1][1][ring_size] == square[2][2][ring_size] == True:
                # Diagonal \
                win = True
        return win


    def checkHorizontal_ar(square):
        win = False
        for row in range(0, 3):
            if square[row][0][0] == square[row][1][1] == square[row][2][2] == True:
                # small -> large
                win = True
            elif square[row][0][2] == square[row][1][1] == square[row][2][0] == True:
                # large -> small
                win = True
        return win


    def checkVertical_ar(square):
        win = False
        for box in range(0, 3):
            if square[0][box][0] == square[1][box][1] == square[2][box][2] == True:
                # small -> large
                win = True
            elif square[0][box][2] == square[1][box][1] == square[2][box][0] == True:
                # large -> small
                win = True
        return win


    def checkDiagonal_ar(square):
        win = False
        if square[2][0][0] == square[1][1][1] == square[0][2][2] == True:
            # Diagonal /, small -> large
            win = True
        elif square[0][0][0] == square[1][1][1] == square[2][2][2] == True:
            # Diagonal \, small -> large
            win = True
        elif square[2][0][2] == square[1][1][1] == square[0][2][0] == True:
            # Diagonal /, large -> small
            win = True
        elif square[0][0][2] == square[1][1][1] == square[2][2][0] == True:
            # Diagonal \, large -> small
            win = True
        return win


    win = False
    while (small > 0) and (medium > 0) and (large > 0) and (win is False):
        random_row = random.choice([0, 1, 2])
        random_box = random.choice([0, 1, 2])
        random_ring = random.choice([0, 1, 2])
        if not square[random_row][random_box][random_ring]:
            sum += 1
            square[random_row][random_box][random_ring] = True
            if random_ring == 0:
                small -= 1
            elif random_ring == 1:
                medium -= 1
            elif random_ring == 2:
                large -= 1
        if not win:
            win = checkHorizontal_eq(square)
        if not win:
            win = checkVertical_eq(square)
        if not win:
            win = checkDiagonal_eq(square)
        if not win:
            win = checkHorizontal_ar(square)
        if not win:
            win = checkVertical_ar(square)
        if not win:
            win = checkDiagonal_ar(square)
    """
        print(random_row,random_box,random_ring, square[random_row][random_box][random_ring])
    
    print(small,medium,large)
    for i in range(0, 3):
        print("---")
        print("row:")
        for j in range(0, 3):
            print("box:")
            for k in range(0, 3):
                print(square[i][j][k])
    """
print(f"Average number of rounds per 100 games: {sum / 100}")
# (duplicate rounds NOT INCLUDED, see lines 107-113)
