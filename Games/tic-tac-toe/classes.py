






class Start_game:

    def __init__(self):
        self.lst = [{'squares_one' : '1', 'squares_two' : '2', 'squares_three' : '3'}, {'squares_4' : '4', 'squares_5' : '5',
'squares_6' : '6'}, {'squares_7' : '7','squares_8' : '8', 'squares_9' : '9'}]

        self.test = self.lst[0]
        self.test2 = self.lst[0]['squares_one']
        self.first_column = [self.lst[0]['squares_one'], self.lst[1]['squares_4'], self.lst[2]['squares_7']]

    def exes(self, user_input):
        print('Player X, it is your turn:  ')
        for item in self.lst:
            for n in item:
                lines = f"__{self.lst[0]['squares_one']}__|__{self.lst[0]['squares_two']}__|__{self.lst[0]['squares_three']}__\n__{self.lst[1]['squares_4']}__|__{self.lst[1]['squares_5']}__|__{self.lst[1]['squares_6']}__\n {self.lst[2]['squares_7']}   | {self.lst[2]['squares_8']}  |  {self.lst[2]['squares_9']}  "
                if user_input == item[n]:
                    item[n] = 'X'
        print(self.lst)
        print(self.test)
        print(self.first_column)
        print(lines)

    def OOOOs(self, user_input):
        print('Player 0, it is your turn:  ')
        for item in self.lst:
            for n in item:
                lines = f"__{self.lst[0]['squares_one']}__|__{self.lst[0]['squares_two']}__|__{self.lst[0]['squares_three']}__\n__{self.lst[1]['squares_4']}__|__{self.lst[1]['squares_5']}__|__{self.lst[1]['squares_6']}__\n {self.lst[2]['squares_7']}   | {self.lst[2]['squares_8']}  |  {self.lst[2]['squares_9']}  "
                if user_input == item[n]:
                    item[n] = 'O'
        print(lines)


    def win_rows_exes(self):
        game_is_on = True

        first_list = self.lst[0]
        second_list = self.lst[1]
        third_list = self.lst[2]

        w = 0

        for n in first_list:
            if first_list[n] == 'X':
                w += 1
        if w == 3:
            print('game over, X wins')
            game_is_on = False
        else:
            pass

        e = 0

        for n in second_list:
            if second_list[n] == 'X':
                e += 1
        if e == 3:
            print('game over, X wins')
            game_is_on = False
        else:
            pass

        t = 0

        for n in third_list:
            if third_list[n] == 'X':
                t += 1
        if t == 3:
            print('game over, X wins')
            game_is_on = False
        else:
            pass

        return game_is_on

    def win_rows_columns(self):

        game_is_on = True

        w = 0

        first_column = (self.lst[0]['squares_one'], self.lst[1]['squares_4'], self.lst[2]['squares_7'])
        second_column = (self.lst[0]['squares_two'], self.lst[1]['squares_5'], self.lst[2]['squares_8'])
        third_column = (self.lst[0]['squares_three'], self.lst[1]['squares_6'], self.lst[2]['squares_9'])

        for n in first_column:
            if n == 'X':
                w += 1
        if w == 3:
            print('game over, X wins')
            game_is_on = False
        else:
            pass

        e = 0

        for n in second_column:
            if n == 'X':
                e += 1
        if e == 3:
            print('game over, X wins')
            game_is_on = False
        else:
            pass

        t = 0

        for n in third_column:
            if n == 'X':
                t += 1
        if t == 3:
            print('game over, X wins')
            game_is_on = False
        else:
            pass

        return game_is_on

    def play_game(self):
        print(f"__{self.lst[0]['squares_one']}__|__{self.lst[0]['squares_two']}__|__{self.lst[0]['squares_three']}__\n__{self.lst[1]['squares_4']}__|__{self.lst[1]['squares_5']}__|__{self.lst[1]['squares_6']}__\n {self.lst[2]['squares_7']}   | {self.lst[2]['squares_8']}  |  {self.lst[2]['squares_9']}")
        print('Enter the number where you would like to place your piece on the board')
        game_on = True

        while game_on:
            print('Player X , it is your turn:  ')
            user_input = input()
            self.exes(user_input)
            if self.win_rows_exes() is False:
                game_on = False
                break
            if self.win_rows_columns() is False:
                game_on = False
                break
            print(self.win_rows_columns())
            print('Player 0, it is your turn:  ')
            user_input = input()
            self.OOOOs(user_input)
            if self.win_rows_exes() is False:
                game_on = False
            if self.win_rows_columns() is False:
                game_on = False




####main gameplay


