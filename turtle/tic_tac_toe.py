#!/usr/bin/env python3                                                                                 
# -*- coding: utf-8 -*-                                                                                
                                                                                                       
###                                                                                                    
# © 2018 The Board of Trustees of the Leland Stanford Junior University                                
# Nathaniel Watson                                                                                     
# nathankw@stanford.edu                                                                                
###

#pip3 install pillow
import pdb
import os
import numpy as np
from PIL import ImageTk
import random
import time
from tkinter import *          
from tkinter.messagebox import showinfo, askyesno

import de_anza_college_academy_2018

root = Tk()
root.title("Lets Play Tic-tac-toe!")

def make_modal(widget):
    widget.focus_set()
    widget.grab_set()
    widget.wait_window()
    return widget


class Board:
    IMAGES_PATH = de_anza_college_academy_2018.IMAGES_PATH

    DEFAULT_PIECE = 0
    X_PIECE = 1
    O_PIECE = 2
    PLAYER_PIECES = {X_PIECE: "X", O_PIECE: "O"}

    GRID_SIZE = 3

    def __init__(self):
        self.container = Frame(root)
        self.container.pack(side=TOP, expand=YES, fill=BOTH)
        self.start_btn = Button(self.container, text="Start", command=self._startup_dialog)
        self.start_btn.pack(side=TOP)
        # The board_frame will use the grid layout manager.
        self.board_frame = Frame(self.container)
        self.board_frame.pack(side=TOP, expand=YES, fill=BOTH)
        # The board has 3 rows and 3 columns. Make it expandable. See Chapter 9 in Programming
        # Python, 4th Ed., by Mark Lutz; particularly the section called
        # "Making Gridded Widgets Expandable". 
        self.board_frame.rowconfigure(0, weight=1)
        self.board_frame.rowconfigure(1, weight=1)
        self.board_frame.rowconfigure(2, weight=1)
        self.board_frame.columnconfigure(0, weight=1)
        self.board_frame.columnconfigure(1, weight=1)
        self.board_frame.columnconfigure(2, weight=1)

        # Default image is a question mark.
        self.default_image = ImageTk.PhotoImage(file=os.path.join(self.IMAGES_PATH,"question_mark_thumb_100.png")) #100x100
        self.images = {}
        self.images[self.X_PIECE] = ImageTk.PhotoImage(file=os.path.join(self.IMAGES_PATH,"tic_tac_toe_x_thumb_100.jpeg")) #100x100
        self.images[self.O_PIECE] = ImageTk.PhotoImage(file=os.path.join(self.IMAGES_PATH,"tic_tac_toe_o_thumb_100.png")) #100x100

        self.board = np.zeros(shape=(self.GRID_SIZE,self.GRID_SIZE),dtype=int)
        # Set self.available_spots. See documentation for method below. 
        self._set_available_spots()
        self.triples = {"rows": {}, "cols": {}, "diags": {}}
        self.triples["rows"][0] = self.board[0]
        self.triples["rows"][1] = self.board[1]
        self.triples["rows"][2] = self.board[2]
        self.triples["cols"][0] = self.board[:,0]
        self.triples["cols"][1] = self.board[:,1]
        self.triples["cols"][2] = self.board[:,2]
        self.triples["diags"][0] = self.board.diagonal()
        self.triples["diags"][1] = np.fliplr(self.board).diagonal()

        #: A `dict` where each key is a two-item tuple representing a position on the game board
        #: ``self.board``, and is of the form (row, col). Each value is the Button object for that
        #: spot, which the user clicks to add their play piece. 
        self.play_space_lookup = {}
        # Set button handlers for play spots:
        for x in range(self.GRID_SIZE):
            for y in range(self.GRID_SIZE):
                b = Button(self.board_frame)
                b.config(image=self.default_image)
                b.grid(row=x, column=y, sticky=NSEW)
                self.play_space_lookup[(x,y)] = b

        root.mainloop()

    def _set_available_spots(self):
        """
        Stores a list of all the unplayed spots on the game board represented by self.board. 
        When a spot is played, the method self._add_piece() removes the relevant item representing 
        this spot in the list. 

        Returns:
            `list`: Each element is a two-item tuple representing the (row, col) position of an unplayed
            spot.
        """
        available_spots = []
        row_cnt = -1
        for row in self.board:
            row_cnt += 1
            col_cnt = -1
            for col in row:
                col_cnt += 1
                available_spots.append((row_cnt,col_cnt)) 
        #: A 3x3 matrix with all values initialized to 0. This represents the game board, and stores
        #: values indicating the game piece played in each spot. The default of 0 means that it is
        #: an unplayed spot. ``Board.X_PIECE`` will be a spot's value when player X selects that spot,
        #: and ``Board.O_PIECE`` will be the value when player O selects that spot. After each player
        #: takes a turn, this object is consulted to check for a winner. 
        self.available_spots = available_spots

    def _startup_dialog(self):
        # Create dialog box to ask user if they'll be X or O.
        tl = Toplevel()
        Label(tl, text="Select your player piece").pack()
        # Create X button
        x_btn = Button(tl, image=self.images[self.X_PIECE])
        x_btn.bind("<Button-1>",(lambda event,selection=self.X_PIECE: self._set_player_piece(event,selection)))
        x_btn.pack(side=LEFT, fill=BOTH)
        # Create O button
        o_btn = Button(tl, image=self.images[self.O_PIECE])
        o_btn.bind("<Button-1>",(lambda event,selection=self.O_PIECE: self._set_player_piece(event,selection)))
        o_btn.pack(side=RIGHT, fill=BOTH)

        # Set button handlers for play spots:
        for btn in self.play_space_lookup.values():
            btn.bind("<Button-1>", self._get_played_spot)

        # A Button's 'state' can be NORMAL/ACTIVE/DISABLED.
        self.start_btn.config(state=DISABLED)
        tl = make_modal(tl)

    def _set_player_piece(self, event, selection):
        # Player 1 is designated to be the one that selects their piece.
        if selection not in self.PLAYER_PIECES:
            raise Exception("Invalid player piece. Must be one of {}.".format(list(self.PLAYER_PIECES.keys())))
        self.player1_piece = selection
        # The person who selected their play piece goes first, so set that to be the current piece. 
        self.current_piece = self.player1_piece
        self.player2_piece= self._get_other_player_piece()
        # close dialog
        event.widget.master.destroy()
        self.computer = askyesno("Computer player?", "Play against the computer?")

    def _get_other_player_piece(self):
        if self.current_piece == self.X_PIECE:
            return self.O_PIECE
        return self.X_PIECE

    def _get_played_spot(self, event):
        widget = event.widget
        self._add_piece(widget)

    def _add_piece(self, played_spot):
        played_spot.config(image=self.images[self.current_piece])
        played_spot.unbind("<Button-1>")
        row = int(played_spot.grid_info()["row"])
        col = int(played_spot.grid_info()["column"])
        self.available_spots.remove((row,col))
        self.board[row][col] = self.current_piece
        self.container.focus_set()
        self.container.update()
        self.check_game_over()

    def _computer_play(self):
        """
        The computer algorithm works by first checking all rows, then all columns, and finally 
        the two diagonals for exactly two plays by the other player. This works as follows:

          1. If any row has exactly two plays by the other player, then the computer will play in 
             the remaining spot in the row if it hasn't been played yet. 
          2. Otherwise, perform the same check as above but using columns instead of rows.
          3. Otherwise, check the two diagonals using the same reasoning as described above. The first 
             diagonal checked is the one spanning the top-left corner of the game board to the 
             bottom right. The other diagonal checked goes from the top-right to the bottom-left of
             the game board.
          4. Otherwise, play at a random spot. 

        Returns:
            `tuple` of the form (row, col) representing the position in the game board for the computer
            to play. 
        """
        spot_loc = None
        other_player_piece = self._get_other_player_piece()
        for row_index in self.triples["rows"]:
            row = self.triples["rows"][row_index]
            col_pos = self._check_two_of_three(player_piece=other_player_piece, row_or_col=row)
            if col_pos != None:
                 spot_loc = (row_index, col_pos)

        if not spot_loc: #try columns
           for col_index in self.triples["cols"]:
               col = self.triples["cols"][col_index]
               row_pos = self._check_two_of_three(player_piece=other_player_piece, row_or_col=col)
               if row_pos != None:
                   spot_loc = (row_pos, col_index)

#        if not spot_loc: #try diags
           for diag_index in self.triples["diags"]:
               diag = self.triples["diags"][diag_index]
               diag_pos = self._check_two_of_three(player_piece=other_player_piece, row_or_col=diag)
               if diag_pos != None:
                   if diag_index == 0: #First diagonal
                       if diag_pos == 0:
                           spot_loc = (0,0)
                       elif diag_pos == 1:
                           spot_loc = (1,1)
                       else:
                           spot_loc = (2,2)
                   else:
                       if diag_pos == 0:
                           spot_loc = (0,2)
                       elif diag_pos == 1:
                           spot_loc = (1,1)
                       else:
                           spot_loc = (2,0)
        if not spot_loc: #then set a random spot
            spot_loc = random.choice(self.available_spots)
        played_spot = self.play_space_lookup[spot_loc]
        self._add_piece(played_spot)

    def _check_two_of_three(self, player_piece, row_or_col):
       """
       Given a row or column from the board ``self.board``, determines whether two of three spots
       have been played with the specified player piece. This is used as a computer algorithm to 
       help the computer know where the play next in order to block the other play at the right 
       position.
 
       Args: 
           player_piece: `int`. Must be one from the set ``[Board.DEFAULT_PIECE, Board.X_PIECE, Board.O_PIECE]``. 
           row_or_col: `list`. A row or column list from the board ``self.board``.

       Returns:
           `None`: If the specified player piece isn't present exactly twice.
           `int`: The index in the supplied list to be played by the computer if the player piece
           is present exactly twice.
       """
       row_or_col = row_or_col.tolist()
       if not row_or_col.count(player_piece) == 2:
           return
       index = -1
       for i in row_or_col:
           index += 1
           if i != player_piece:
               if i == Board.DEFAULT_PIECE:
                   return index
       return
                
    def check_game_over(self):
        """
        Determines the state of the game, which can be over, a stalemate, of in progress. 

        If the game is over, meaning that one of the players has won, a congratulary prompt appears
        and asks the user whether they'd like to play again or quite.

        If the game is a stale mate, an info message is displayed and the board is then reset automatically
        in preparation for another game. 

        If neither of the two above conditions are found to be true, then this function has no affect. 
        """
        game_over = False
        for triple_type in self.triples: #row, col, or diag
            for triple_index in self.triples[triple_type]:
                triple = self.triples[triple_type][triple_index]
                set_triple = set(triple)
                if len(set_triple) == 1:
                    # Make sure that the values aren't all the default piece of 0
                    if not set_triple.pop() == Board.DEFAULT_PIECE:
                        game_over = True

        if not game_over and not self.available_spots:
            showinfo("Stalemate", "Nobody wins this round!")
            self.reset()
        elif game_over:
            if askyesno("Congratulations!","Player {} has won! Play again?".format(self.PLAYER_PIECES[self.current_piece])):
                self.reset()
            else:
                root.quit()
        else:
            self.current_piece = self._get_other_player_piece()
            if self.computer and self.current_piece == self.player2_piece:
                root.after(600,self._computer_play)

    def reset(self):
        """Resets the board to allow the user to play another game.
        """
        for btn in self.play_space_lookup.values():
            btn.config(image=self.default_image)
            #Make sure all buttons have a handle again:
            btn.bind("<Button-1>", self._get_played_spot)

            # Unbind handlers for play spots that weren't played:
            #btn.unbind("<Button-1>")
        #self.start_btn.config(state=ACTIVE)
        self.board.fill(0)    
        self._set_available_spots()
        
if __name__ == "__main__":
    Board()
