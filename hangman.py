#!PythonProjects/env python
# Davenport University
# Class Info: CISP253-23151 (Winter 2022)
# Author: Alexander Rogers
# Contact: arogers23@email.davenport.edu

# Program name: hangman.py
"""
Example of how a Python programs can use modules, classes, functions, file handling, and methods can be used to
create the game of Hangman. The project uses the tkinter module in the graphics file, which was created by
John Zelle.
"""

# Import the required modules and functions

from random import randint
from graphics import *


# Class defines the container from which objects are handled in. The class Game will store all of the functions
# neccessary to run the Hangman game.
class Game:
    def __init__(self, win_width, win_height):
        self.width = 500
        self.height = 460
        self.width = win_width
        self.height = win_height

    def easy(self):
        """
            easy function with try/except statement to ensure the files existence in the folder.
               Args:
                   self argument: instance of the class.
               Returns:
                   Try to return value is the file, labelled as file_name, except if the file is not in the folder.
        """
        # This function checks for a file called "easy.txt". Which contains the easy list of words the game can use.
        # These words are 3-4 letters long.
        # If it exists in the same directory as the Hangman game, then we use this file as our word list if chosen.
        try:
            file_name = open('easy.txt', 'rt')
            return file_name
        except IOError:
            print('Error 1: File not specified')
            exit()

    def medium(self):
        """
            medium function with try/except statement to ensure the files existence in the folder.
               Args:
                   self argument: instance of the class.
               Returns:
                   Try to return value is the file, labelled as file_name, except if the file is not in the folder.
        """
        # This function checks for a file called "medium.txt". Which contains the easy list of words the game can use.
        # These words are 5-7 letters long.
        # If it exists in the same directory as the Hangman game, then we use this file as our word list if chosen.
        try:
            file_name = open('medium.txt', 'rt')
            return file_name
        except IOError:
            print('Error 1: File not specified')
            exit()

    def hard(self):
        """
            hard function with try/except statement to ensure the files existence in the folder.
               Args:
                   self argument: instance of the class.
               Returns:
                   Try to return value is the file, labelled as file_name, except if the file is not in the folder.
        """

        # This function checks for a file called "hard.txt". Which contains the easy list of words the game can use.
        # These words are 8 letters long.
        # If it exists in the same directory as the Hangman game, then we use this file as our word list if chosen.
        try:
            file_name = open('hard.txt', 'rt')
            return file_name
        except IOError:
            print('Error 1: File not specified')
            exit()

    # This function displays to the window a Hangman element when an incorrect letter is guessed. The element that
    # is displayed depends on the number of fails that the player has accumulated throughout the game.
    def draw_hangman(self, fail, win, win_hangmanpic):

        """
            draw_hangman function with if/elif statement to draw Hangman elements into the window based on the number
            of attempts left.
               Args:
                   self argument: instance of the class.
                   fail argument: the second parameter, defaults to zero.
                   win argument: the third parameter, captures window instance and initializes an area for output.
                   win_hangmanpic: the fourth parameter, returns values from if/elif statements to a list in the
                   gameplay loop.

               For each loop, at least one new element is added to the Hangman diagram.
               Note:
                   Include the `self` parameter in the argument section.
                   All window height and width values are integers representing pixels. Ex: win_width = 500 is
                   window that is 500 pixels wide.
        """

        # All coordinates are pixels, and coordinates are dependent on window size (width and height).
        win_width = 500
        hangman_yaxis = win_width / 2.2
        if fail == 1:

            # Failed attempt 1: Reveal the Hangman's post
            line1 = Line(Point(win_width - win_width / 3, 100), Point(win_width - win_width / 3, 300))
            line1.draw(win)
            win_hangmanpic.append(line1)
            line2 = Line(Point(win_width - win_width / 3, 300), Point(hangman_yaxis, 300))
            line2.draw(win)
            win_hangmanpic.append(line2)
            line3 = Line(Point(hangman_yaxis, 300), Point(hangman_yaxis, 270))
            line3.draw(win)
            win_hangmanpic.append(line3)

        elif fail == 2:

            # Failed attempt 2: Reveal the Hangman's head
            circle4 = Circle(Point(hangman_yaxis, 254), 16)
            circle4.draw(win)
            win_hangmanpic.append(circle4)

        elif fail == 3:

            # Failed attempt 3: Reveal the Hangman's body
            line5 = Line(Point(hangman_yaxis, 238), Point(hangman_yaxis, 180))
            line5.draw(win)
            win_hangmanpic.append(line5)

        elif fail == 4:

            # Failed attempt 4: Reveal the Hangman's left arm
            line6 = Line(Point(hangman_yaxis, 225), Point(hangman_yaxis - 20, 200))
            line6.draw(win)
            win_hangmanpic.append(line6)

        elif fail == 5:

            # Failed attempt 5: Reveal the Hangman's right arm
            line7 = Line(Point(hangman_yaxis, 225), Point(hangman_yaxis + 20, 200))
            line7.draw(win)
            win_hangmanpic.append(line7)

        elif fail == 6:

            # Failed attempt 6: Reveal the Hangman's left leg
            line8 = Line(Point(hangman_yaxis, 180), Point(hangman_yaxis - 15, 135))
            line8.draw(win)
            win_hangmanpic.append(line8)

        elif fail == 7:

            # Failed attempt 7: Reveal the Hangman's right leg
            line9 = Line(Point(hangman_yaxis, 180), Point(hangman_yaxis + 15, 135))
            line9.draw(win)
            win_hangmanpic.append(line9)

            # Reveal the full Hangman diagram, including eyes, and mouth
            line10 = Line(Point(hangman_yaxis + 7, 260), Point(hangman_yaxis + 2, 255))
            line10.draw(win)
            win_hangmanpic.append(line10)
            line11 = Line(Point(hangman_yaxis + 2, 260), Point(hangman_yaxis + 7, 255))
            line11.draw(win)
            win_hangmanpic.append(line11)
            line12 = Line(Point(hangman_yaxis - 7, 260), Point(hangman_yaxis - 2, 255))
            line12.draw(win)
            win_hangmanpic.append(line12)
            line13 = Line(Point(hangman_yaxis - 2, 260), Point(hangman_yaxis - 7, 255))
            line13.draw(win)
            win_hangmanpic.append(line13)
            line14 = Line(Point(hangman_yaxis - 7, 247), Point(hangman_yaxis + 7, 247))
            line14.draw(win)
            win_hangmanpic.append(line14)

    # Initializes the INSTRUCTIONS window, which is available within the HANGMAN window upon game difficulty selection.
    def instr(self):
        """
            instr function that initilizes the INSTRUCTION window.
                Args:
                    self argument: instance of the class.

                    The file is opened and read to the Text point within window.

                Note: uses own win_width and win_height since the text used comes within the README file which is
                static.
        """
        win_width = 800
        win_height = 900

        # Chooses the file to display as text in the window.
        file = open('README.txt')
        text = file.read()

        # Initialize the INSTRUCTIONS window.
        win = GraphWin("INSTRUCTIONS", win_width, win_height)
        win.setCoords(0, 0, win_width, win_height)
        win_message = Text(Point(win_width / 2, 450), text)
        win_message.setStyle('bold')
        win_message.setSize(10)
        win_message.draw(win)

    # Initializes the PAUSED window, which is available within the HANGMAN window upon menu selection.
    def popup(self):
        """
            popup function that initializes the PAUSED window.
              Args:
                   self argument: instance of the class
              While:
                    select variable is set to False, as no instance of its existence has been recorded, once recorded,
                    the variable is set to True.
              Returns:
                    The function returns a 1 which signifies a selection to go to the main menu,
                    else the function returns a 0, meaning that nothing has incurred, leaving a static window.
              Note:
                    uses own win_width and win_height since the window is to remain static.

        """
        win_width = 500
        win_height = 460
        win = GraphWin("PAUSED", win_width, win_height)
        win.setCoords(0, 0, win_width, win_height)
        win_message = Text(Point(win_width / 2, 400), "GO BACK TO MAIN MENU?")
        win_message.setStyle('bold')
        win_message.draw(win)

        # Draw the Main Menu button and text.
        win_butpopup = Rectangle(Point(200, 300), Point(300, 350))
        win_butpopup.setFill(color_rgb(255, 255, 255))
        win_butpopup.setOutline(color_rgb(0, 0, 0))
        win_butpopup.draw(win)
        win_butpopup_label = Text(Point(250, 325), 'Main Menu')
        win_butpopup_label.setTextColor(color_rgb(0, 0, 0))
        win_butpopup_label.draw(win)
        select = False
        while select is False:
            # Sets the mouse as an input option in the window, and records mouse click coordinates.
            p = win.getMouse()
            if p.getX() <= 300 and p.getY() <= 350:
                select = True
        # Sets value of the variable select to True, which is passed along to the restart function.
        if select is True:
            win.close()
            return 1
        else:
            return 0

    # Takes input from the popup function, and brings the game back to the MAIN MENU, losing progress of the current
    # game.
    def restart(self, win):
        """
            restart function with if/elif statement to determine if the game is to be restarted after the selection from
            the popup function.
              Args:
                    self argument: instance of the class.
                    win argument: the second parameter, and captures the window instance.

                    In the loop, the choice variable is set to the result of the popup function, which is either a
                    static  0, or a returned 1.
              Note:
                    Include the `self` parameter in the argument section.
        """
        choice = Game.popup(self)
        if choice == 1:
            win.close()
            return Game.main(self)
        elif choice == 0:
            exit()

    # Carries out the menu functionality of the game, allowing the user to select between 3 different difficulties.
    # The buttons of the window are also displayed, and correspond to the functions above.
    def menu_selection(self):
        """
           menu_selection function that initializes the MAIN MENU window, and communicates to the main function the game
           difficulty, and the word chosen within that difficulty for the game.
               Args:
                    self argument: instance of the class
               While:
                    select variable is set to False, as no instance of its existence has been recorded,
                    once recorded, the variable is set to an integer value to represent the difficulty requested.
               Returns:
                    The function returns the game_word variable, which is the word that will be used in the Hangman
                    game, and the length of the word which is revealed to the user.
               Note: uses own win_width and win_height since the window is to remain static.

        """
        win_width = 500
        win_height = 460
        win = GraphWin("MAIN MENU", win_width, win_height)
        win.setCoords(0, 0, win_width, win_height)

        win_message = Text(Point(win_width / 2, 400), "Welcome to Hangman: The Game! \n Select a difficulty")
        win_message.setStyle('bold')
        win_message.draw(win)

        # Draw the Easy button and the text inside.
        win_buteasy = Rectangle(Point(5, 30), Point(90, 0))
        win_buteasy.setFill(color_rgb(50, 50, 204))
        win_buteasy.setOutline(color_rgb(0, 0, 0))
        win_buteasy.draw(win)
        win_butinst_label = Text(Point(46, 15), 'Easy')
        win_butinst_label.setTextColor(color_rgb(0, 0, 0))
        win_butinst_label.draw(win)

        # Draw the Medium button and the text inside.
        win_butmedium = Rectangle(Point(210, 30), Point(300, 0))
        win_butmedium.setFill(color_rgb(0, 255, 0))
        win_butmedium.setOutline(color_rgb(0, 0, 0))
        win_butmedium.draw(win)
        win_butmedium_label = Text(Point(255, 15), 'Medium')
        win_butmedium_label.setTextColor(color_rgb(0, 0, 0))
        win_butmedium_label.draw(win)

        # Draw the Hard button and the text inside.
        win_buthard = Rectangle(Point(420, 30), Point(500, 0))
        win_buthard.setFill(color_rgb(255, 50, 0))
        win_buthard.setOutline(color_rgb(0, 0, 0))
        win_buthard.draw(win)
        win_buthard_label = Text(Point(460, 15), 'Hard')
        win_buthard_label.setTextColor(color_rgb(0, 0, 0))
        win_buthard_label.draw(win)
        select = False
        while select is False:
            p = win.getMouse()
            if p.getX() <= 90 and p.getY() <= 30:
                select = 1
            elif 300 >= p.getX() >= 210 and p.getY() <= 30:
                select = 2
            elif p.getX() >= 420 and p.getY() <= 30:
                select = 3

        # Easy difficulty
        if select == 1:
            select = Game.easy(self)
            win.close()

        # Medium difficulty
        if select == 2:
            select = Game.medium(self)
            win.close()

        # Hard difficulty
        if select == 3:
            select = Game.hard(self)
            win.close()

        else:
            win.close()

        # The following expressions choose word randomly from the list of words taken from the input file
        file_name = select
        words = file_name.readlines()
        word_total = len(words)
        ran_num = randint(0, word_total - 1)
        game_word = words[ran_num].replace('\n', '')
        word_len = len(game_word)
        return game_word, word_len

    def main(self):
        """
           main function initializes the HANGMAN window, uses if/elif/else statements to processes the input of the user
           and displays the results of the game, determines if the user wants to exit the game, or play the game again.
                Args:
                    self argument: instance of the class
                While:
                    The fails variable is set to 0, and while the recorded fails does not progress pass 7, as well
                    as the variable victory being recorded as False, the game has not been completed, and continues.
                if:
                    The iteration of if statements sets the graphics module function of getting mouse coordinates,
                    and determining if a click has been picked up within the boundaries of the determined grid.
                    if/elif/else/continue
                        The iteration of if statements is the processing logic behind the recording the guesses by
                        the user, determining if the letter has already been guessed, if the guess is indeed in the
                        game word, and if the game word has been found through successful guess atempts. If the game
                        is won by the user, victory is set to true, and confirmation is drawn to the screen. Else,
                        the user has run out of guess attempts, and fails the game.
                    if/elif/else/for
                        The post_game_select variable is set to False, while post game is not False, the two choices
                        of post_game_selection being set to 1 or 2 are given in the form of quitting the game, or
                        playing the game again. Hence, if set to 1, the game will clear all items in the window
                        and be brought back to the main menu to be played again by reinitializing the main function,
                        and if set to 2, the game will be exited.
                Note: uses own win_width and win_height since the window is to remain static, unless being drawn to
                        which occurs when the letters guessed which are not in the game word are appended to the window.

        """
        # Initialize the word for the game, and the length of the word from the selected menu difficulty.
        game_word, word_len = Game.menu_selection(self)

        # Build the grid of empty spaces, one space for each letter of the chosen word
        grid = '__'
        for i in range(word_len - 1):
            grid = grid + ' __'

        win_width = 500
        win_height = 460
        win = GraphWin("HANGMAN", win_width, win_height)
        win.setCoords(0, 0, win_width, win_height)

        # Draw to the window the game message area, the ground of the Hangman diagram, and the empty playing grid.
        win_message = Text(Point(win_width / 2, 70), "Hangman! Guess a letter to begin!.")
        win_message.setStyle('bold')
        win_message.draw(win)
        win_ground = Line(Point(win_width / 10, 100), Point(win_width - win_width / 10, 100))
        win_ground.draw(win)
        win_grid = Text(Point(win_width / 2, win_height - 70), grid)
        win_grid.draw(win)

        # Draw to the window the letter guess area, and the text of the letter guess area.
        win_guesstxt = Text(Point(win_width / 2 - 35, 30), "Enter a letter: ")
        win_guesstxt.draw(win)
        win_guessinput = Entry(Point(win_width / 2 + 30, 28), 2)
        win_guessinput.draw(win)
        win_guessinput.setText('')

        # Draw to the window the Guess button area, and the text of the Guess button.
        win_butguess = Rectangle(Point(win_width / 2 + 55, 43), Point(win_width / 2 + 130, 13))
        win_butguess.setFill(color_rgb(100, 250, 255))
        win_butguess.setOutline(color_rgb(0, 0, 0))
        win_butguess.draw(win)
        win_butguess_label = Text(Point(win_width / 2 + 92, 28), 'Guess')
        win_butguess_label.setTextColor(color_rgb(0, 0, 0))
        win_butguess_label.draw(win)

        # Draw to the window the wrong guessed letters area, and the letters that go in the area which are appended to
        # w_letters.
        w_letters = []
        win_letter = Rectangle(Point(175, 330), Point(325, 360))
        win_letter.setFill(color_rgb(255, 255, 255))
        win_letter.setOutline(color_rgb(0, 0, 0))
        win_letter.draw(win)
        win_letters = Text(Point(win_width / 2, 345), w_letters)
        win_letters.setTextColor(color_rgb(0, 0, 0))
        win_letters.draw(win)

        # Draw to the window the Instructions button area, and the text of the Instructions button.
        win_butinst = Rectangle(Point(4, 30), Point(90, 0))
        win_butinst.setFill(color_rgb(255, 255, 255))
        win_butinst.setOutline(color_rgb(0, 0, 0))
        win_butinst.draw(win)
        win_butinst_label = Text(Point(46, 15), 'Instructions')
        win_butinst_label.setTextColor(color_rgb(0, 0, 0))
        win_butinst_label.draw(win)

        # Draw to the window the Menu button area, and the text of the Menu button.
        win_butpopup = Rectangle(Point(440, 400), Point(500, 425))
        win_butpopup.setFill(color_rgb(0, 200, 0))
        win_butpopup.setOutline(color_rgb(0, 0, 0))
        win_butpopup.draw(win)
        win_butpopup_label = Text(Point(470, 412), 'Menu')
        win_butpopup_label.setTextColor(color_rgb(0, 0, 0))
        win_butpopup_label.draw(win)

        # The game logic is initialized with the fail counter to 0, guessed_letters list empty, win_hangmanpic list
        # empty (meaning no Hangman elements currently initialized in the window. Finally, the status of the game or
        # victory in this case, is set to False.
        fails = 0
        guessed_letters = []
        win_hangmanpic = []
        victory = False
        while fails < 7 and victory is False:

            # Record the player's mouse click location.
            p = win.getMouse()

            # INSTRUCTIONS window.
            if p.getX() <= 90 and p.getY() <= 30:
                Game.instr(self)

            # PAUSED window.
            if 500 >= p.getX() >= 440 and p.getY() > 400:
                Game.restart(self, win)

            # Anything else, continue the while loop.
            if p.getX() < win_width / 2 + 55 or p.getX() > win_width / 2 + 130 or p.getY() < 13 or p.getY() > 43:
                continue

            # Record the guessed letter, and if it's not in the word, run the top of the loop and attempt another guess.
            guess = win_guessinput.getText().lower()
            win_guessinput.setText('')
            if guess == ' ' or guess == '' or len(guess) != 1:
                if len(guess) != 1:
                    win_message.setText("Please only guess a single letter at a time. Try again!")
                continue

            # If the guessed letter is in the game word, and it hasn't been guessed yet by the user, then update
            # the grid by placing this letter in the respective empty space(s) on the grid.
            if guess in game_word.lower() and not (guess in guessed_letters):
                guessed_letters.append(guess)
                grid = game_word
                for letter in game_word:
                    if (not (letter.lower() in game_word) or not (letter.lower() in guessed_letters)) and letter != ' ':
                        grid = grid.replace(letter, ' __ ')

                    win_grid.setText(grid)

                if grid == game_word:
                    victory = True
                else:
                    win_message.setText(f"{guess.upper()} is in the word.")

            # This letter has been previously guessed, therefore alerting the user.
            elif guess in guessed_letters:
                win_message.setText(f"{guess.upper()} has already been guessed!")

            # This letter is not in the game word, and his counted as a fail toward the fail counter. The Hangman
            # is then given an element based on the fail number the user is on.
            # Additionally, the letters that are not in the word are appended to the wrong letters area in the window.
            else:
                guessed_letters.append(guess)
                w_letters.append(guess)
                fails = fails + 1
                win_message.setText(f"{guess.upper()} is a wrong guess! Try another letter.")
                win_letters.undraw()
                win_letters.draw(win)
                Game.draw_hangman(self, fails, win, win_hangmanpic)

        # If the user reaches the fail count limit of 7, or victory is False still, or Victory is True,
        # then the game is over. The following removes all the buttons and text in the window, and replaces
        # them with the game word. Other elements are determined in the if statements below.
        win_guesstxt.undraw()
        win_guessinput.undraw()
        win_butguess.undraw()
        win_butguess_label.undraw()
        win_butinst.undraw()
        win_butinst_label.undraw()
        win_letters.undraw()
        win_letter.undraw()
        win_butpopup_label.undraw()
        win_butpopup.undraw()
        win_message.move(0, -10)

        win_grid.setText(game_word.upper())
        win_grid.setStyle('bold')
        win_grid.setSize(16)

        # If the game is won, the message at the bottom of the window to reflect a win, and draw a crudely made
        # smiley face.
        if victory is True:
            win_message.setText("Congrats! You've guessed the word correctly.")
            win_message.setTextColor(color_rgb(0, 120, 0))
            win_grid.setTextColor(color_rgb(0, 120, 0))

            for hm_obj in win_hangmanpic:
                hm_obj.undraw()
            win_hangmanpic = []
            circle1 = Circle(Point(win_width / 2, 240), 110)
            circle1.setOutline(color_rgb(0, 120, 0))
            circle1.setFill(color_rgb(126, 236, 53))
            circle1.draw(win)
            win_hangmanpic.append(circle1)
            eye1 = Circle(Point(win_width / 2 - 40, 285), 20)
            eye1.setOutline(color_rgb(0, 120, 0))
            eye1.draw(win)
            win_hangmanpic.append(eye1)
            eye2 = eye1.clone()
            eye2.move(80, 0)
            eye2.draw(win)
            win_hangmanpic.append(eye2)
            eye1_inner = Circle(Point(win_width / 2 - 40, 285), 5)
            eye1_inner.setFill(color_rgb(0, 120, 0))
            eye1_inner.setOutline(color_rgb(0, 120, 0))
            eye1_inner.draw(win)
            win_hangmanpic.append(eye1_inner)
            eye2_inner = eye1_inner.clone()
            eye2_inner.move(80, 0)
            eye2_inner.draw(win)
            win_hangmanpic.append(eye2_inner)
            mouth = Circle(Point(win_width / 2, 200), 50)
            mouth.setFill(color_rgb(0, 120, 0))
            mouth.setOutline(color_rgb(0, 120, 0))
            mouth.draw(win)
            win_hangmanpic.append(mouth)
            mouth_cover = Rectangle(Point(win_width / 2 - 50, 200), Point(win_width / 2 + 50, 250))
            mouth_cover.setFill(color_rgb(126, 236, 53))
            mouth_cover.setOutline(color_rgb(126, 236, 53))
            mouth_cover.draw(win)
            win_hangmanpic.append(mouth_cover)

        # Otherwise, the text will reflect a loss, and change the Hangman diagram to red, with X's over his eyes
        # and a mouth.
        else:
            win_message.setText("Sorry! You didn't completely guess the word.")
            win_message.setTextColor(color_rgb(170, 0, 0))
            win_grid.setTextColor(color_rgb(170, 0, 0))

            i = 0
            for hm_obj in win_hangmanpic:
                if i == 3:
                    hm_obj.setOutline(color_rgb(170, 0, 0))
                else:
                    hm_obj.setFill(color_rgb(170, 0, 0))
                i = i + 1

        # Draw a button to the window asking if the user wants to play the game again.
        win_butagain = Rectangle(Point(win_width - 90, 30), Point(win_width, 0))
        win_butagain.setFill(color_rgb(126, 236, 53))
        win_butagain.setOutline(color_rgb(0, 110, 0))
        win_butagain.draw(win)
        win_butagain_label = Text(Point(win_width - 45, 15), 'Play again?')

        win_butagain_label.setTextColor(color_rgb(0, 110, 0))
        win_butagain_label.draw(win)

        # Draw a button to the window asking if the user wants to quit the game.
        win_butquit = Rectangle(Point(4, 30), Point(54, 0))
        win_butquit.setFill(color_rgb(255, 177, 177))
        win_butquit.setOutline(color_rgb(170, 0, 0))
        win_butquit.draw(win)
        win_butquit_label = Text(Point(29, 15), 'Quit')

        win_butquit_label.setTextColor(color_rgb(170, 0, 0))
        win_butquit_label.draw(win)

        # This will check for an action to be selected by the user, returning a the Main Menu, or completely exiting
        # the game
        post_game_select = False
        while not post_game_select:
            p = win.getMouse()

            # Play again?
            if p.getX() >= (win_width - 90) and p.getY() <= 30:
                post_game_select = 1

            # Quit
            elif p.getX() <= 54 and p.getY() <= 30:
                post_game_select = 2

        # If 1 is initialized to post_game_select, then remove all the window elements, and return to the Main Menu.
        if post_game_select == 1:
            win_objs = [win_message, win_ground, win_grid, win_butagain, win_butagain_label, win_butquit,
                        win_butquit_label, win_hangmanpic]
            for obj in win_objs:
                if obj == win_hangmanpic:
                    for hm_obj in win_hangmanpic:
                        hm_obj.undraw()
                else:
                    obj.undraw()

            win.close()
            Game.main(self)

        # Else 2 is initialized to post_game_select, and executes the exit code function.
        else:
            exit()


if __name__ == "__main__":
    Game.main(True)
# EOF #
