'''
Othello is played as follows: Each Othello piece is white on one side and black on the other.
When a piece is surrounded by its opponents on both the left and right sides, or both the top and
bottom, it is said to be captured and its color is flipped. On your turn, you must capture at least one
of your opponent's pieces. The game ends when either user has no more valid moves. The win is
assigned to the person with the most pieces. Implement the object-oriented design for Othello.
'''
'''
How big is the board? -> 8x8
How does the game begin? W (3, 3), B (3, 4), B (4, 3), W (4, 4)
    ->      W B
            B W
So we don't assume diagonal counts as capturing
If a row of pieces are captured, it should not result in additional rows/columns captured as a result of the initial capture
Each move must result in a capture or else the game is over
Person with the most pieces wins
Black always goes first
Max of 32 pieces per Player
Cant place a piece outside of the board

Core objects:
    Board
    Othello Piece (color attribute: black or white?)
    Player (player will be black or white?)

Relationships
    - There can only be one board - Singleton design pattern? You lose to ability to instantiate multiple times
    - There are only 2 players
    - A player can only place/move the color of the othello piece its assigned to
    - A board will have many othello pieces

Actions:
    Board
        - Should be able to know how many black and white pieces on the board at any turn
        - Should know the exact locations of each black and white piece on the board at any turn
        - Should know what move a player can make at any turn.
            - Should be able to know which othello pieces to convert to the opposite color.
                - THis is triggered by the player when a player places an othello piece on a valid location
            - Should be able to know when the game is over -> no more players can place a piece.
                - This should be checked after every time a player places an Othello piece
            - Should be able to deny Player action if they try to make an invalid move -> We check the user input
        - Should know how to initialize the board with 2 whites and 2 blacks
        - Should know how to keep track of the score. Who updates the score?
            - The board does the actual updating/calculating of the score but the Player is the one
            that should trigger this event. This event is triggered when a new piece is on the board and
            then pieces are captured.

    Player
        - Places one Othello piece on the board
        - Player needs to be assigned a color either black or white and a player can only use one color for the entirety of the game
        - If player is black then the that player goes first


    OthelloPiece
        - Can be either black or white
        - Can change its own color. Will be triggered by the board

'''

class Game():

    def __init__(self, p1_name, p2_name):
        self.scores = {'black': 0, 'white': 0}
        self.players = [Player(p1_name, 'black'), Player(p2_name, 'white')]
        self.board = Board()

    def _change_score(self, color, amount_to_change):
        pass

    def _move_exists_for(self):
        pass

    def start(self):
        pass

        # get max score


class Board():

    NUM_OF_ROWS = 10
    NUM_OF_COLS = 10

    def __init__(self):
         self.__board = [[None] * NUM_OF_ROWS for _ in range(NUM_OF_COLS)]


    def insert_piece(self, piece, row, column):
        # Need to validate player's row and column choice
        if not self._validate_move(row, column):
            print('Invalid move. Try again')
            return False

        # place the piece on the board
        # score updates
        # based on where the piece was placed, determine which pieces to flip
        # flip each piece and change the score accordingly for each color
        self.__board[row][column] = piece
        self._flip_pieces(self, piece.color)
        return True

    def _validate_move(self, row, column):
        pass

    def _flip_pieces(self, color):
        # flips pieces and updates score
        pass

class Player():

    def __init__(self, name, color):
        self.name = name
        self.color = color

    @property
    def color(self):
        return self._color

    @property.setter
    def color(self, value):
        if value.lower() not in ['black', 'white']:
            raise ValueError('Color must be black or white.')
        self._color = value

    def play_piece(self, row, column):
        '''
        Can call Board instance and assume it's a singleton or create an interface/contract
        between the Player class and the Board class to interact to prevent tight coupling
        '''


class Piece():

    def __init__(self, color):
        self.color = color
