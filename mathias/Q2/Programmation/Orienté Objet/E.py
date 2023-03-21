import random

class Board :
    def __init__(self, size:int=6) :
        self.size = size
        self.wall = [] #tuples list
        self.player = None
        self.score_list = []

    def draw(self):
        for i in range(self.size):
            for j in range(self.size):
                if (i,j) == self.player.position :
                    print("O", end=" ")
                elif (i,j) in self.wall :
                    print("X", end=" ") 
                else :
                     print(".", end=" ") 
            print()

    def pop_wall(self) :
        new_wall = (random.randrange(0, self.size, 1),random.randrange(0, self.size, 1))
        while new_wall in self.wall or new_wall == (0,0) or new_wall == (self.size-1,self.size-1) :
            new_wall = (random.randrange(0, self.size, 1),random.randrange(0, self.size, 1))
        self.wall.append(new_wall)

    def check_death(self) :
        is_dead = False
        for wall in self.wall :
            if self.player.position == wall : is_dead = True
        if self.player.position[0] == -1\
        or self.player.position[1] == -1\
        or self.player.position[0] == self.size\
        or self.player.position[1] == self.size :
            is_dead = True
        return is_dead

    def check_win(self) :
        return self.player.position == (self.size-1, self.size-1)
    
    def best_player(self) :
        best_score = float('-inf')
        best_player = None  
        for score in self.score_list:
            for player, score_player in score.items():
                if score_player > best_score:
                    best_score = score_player
                    best_player = player
        return best_player

    def play_game(self) :
        print("Hello "+self.player.name+" !")
        while self.check_death() == False and self.check_win() == False :
            self.pop_wall()
            self.draw()
            self.player.move()
            self.player.score -= 1
        if self.check_death() == True :
            print("you are dead, noob")
            print("Your score is : 0")
            self.score_list.append({self.player.name : 0})
            print("The actual best player is "+str(self.best_player())+" !")
        elif self.check_win() == True :
            print("GG, well play")
            print("Your score is : "+str(self.player.score))
            self.score_list.append({self.player.name : self.player.score})
            print("The actual best player is "+str(self.best_player())+" !")          


class Player :
    def __init__(self, name:str) :
        self.name = name
        self.position = (0,0)
        self.keyboard_key = {"z":(-1,0), "d":(0,1), "s":(1,0), "q":(0,-1)}
        self.board = None
        self.score = 30

    def move(self) :
        move = self.keyboard_key[str(input(">>> "))]
        while self.position[0] + move[0] == -1\
        or self.position[1] + move[1] == -1\
        or self.position[0] + move[0] == self.board.size\
        or self.position[1] + move[1] == self.board.size :
            print("Error")
            move = self.keyboard_key[str(input(">>> "))]
        self.position = (self.position[0] + move[0], self.position[1] + move[1])


if __name__ == "__main__" :
    is_want_replay = None

    #Create a new player
    player_name = str(input("Enter a player name : "))
    player = Player(player_name)

    #Setup the game
    game = Board(size=7)
    game.player = player
    player.board = game
    keyboard_key = {"z":(-1,0), "d":(0,1), "s":(1,0), "q":(0,-1)}
    game.play_game()

    #Replay
    is_want_replay = None
    is_want_replay = str(input("Play again ? (y/n): "))
    while is_want_replay != "y" or is_want_replay != "n" :
        is_want_replay = str(input("Play again ? (y/n): "))

        #Create a new player
        player_name = str(input("Enter a player name : "))
        player = Player(player_name)

        #Setup the game
        game.wall.clear()
        game.player = player
        player.board = game
        keyboard_key = {"z":(-1,0), "d":(0,1), "s":(1,0), "q":(0,-1)}
        game.play_game()

        #Replay
        is_want_replay = None
        is_want_replay = str(input("Play again ? (y/n): "))
        while is_want_replay != "y" or is_want_replay != "n" :
            is_want_replay = str(input("Play again ? (y/n): "))
