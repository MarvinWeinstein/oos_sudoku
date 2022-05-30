import random

###############################################################################
#   Klasse Sudoku   ###########################################################
###############################################################################

'''
Die Klasse Sudoku beinhaltet das Sudoku in gelöster und ungelöster Form 
und stellt diverse Funktionen zur Überprüfung der Eingaben und zum 
automatischen Ausfüllen bereit.
'''
class Sudoku:
    sudoku_counter = 0

    def __init__(self, solved, unsolved):
        self.solved = solved
        self.unsolved = unsolved
        self.in_progress = unsolved
        self.full = False
        self.id = Sudoku.sudoku_counter
        print("Neues Sudoku angelegt. ID:", self.id)
        Sudoku.sudoku_counter += 1

    '''
    check_full überprüft, ob das aktuelle Sudoku vollständig ausgefüllt ist.
    '''
    def check_full(self):
        print("sudoku.check_full()")
        check_full = True
        for cell in self.in_progress:
            if cell == "":
                check_full = False
        if check_full:
            print("--- full ---")
        else:
            print("--- not full ---")
        return check_full

    '''
    find_error überprüft, ob im aktuellen Sudoku wenigstens ein Feld 
    fehlerhaft ausgefüllt wurde.
    '''
    def find_error(self):
        print("sudoku.find_error()")
        for i in range(81):
            if self.in_progress[i] != "" and \
                    self.in_progress[i] != self.solved[i]:
                print("--- error found ---")
                return True
        print("--- no error found ---")
        return False

    '''
    hint sucht ein zufälliges nicht ausgefülltes Feld im aktuellen Sudoku und 
    trägt den korrekten Wert ein.
    '''
    def hint(self):
        print("sudoku.hint()")
        empty_cells = []
        for i in range(81):
            if self.in_progress[i] == "":
                empty_cells.append(i)
        random_index = random.randint(0, len(empty_cells)-1)
        hint_index = empty_cells[random_index]
        self.in_progress[hint_index] = self.solved[hint_index]
        print("--- hint given in cell", hint_index, "- value:",
              self.solved[hint_index], "---")
        return hint_index



###############################################################################
#   Einzelne Sudokus hinzufügen   #############################################
###############################################################################

'''
beginner erstellt ein sehr einfaches Sudoku
'''
def beginner():
    unsolved = [9, 2, 4, "", "", 8, 7, "", "",
                7, 1, "", "", 5, "", "", 2, "",
                5, "", "", 2, "", "", "", "", 6,
                "", "", 3, 1, "", 9, "", "", 5,
                "", 5, "", "", 7, "", "", 6, "",
                4, "", "", 8, "", 5, 9, "", "",
                6, "", "", "", "", 2, "", "", 9,
                "", 8, "", "", 9, "", "", 7, 4,
                "", "", 5, 7, "", "", 2, 8, 3]
    solved = [9, 2, 4, 6, 3, 8, 7, 5, 1,
              7, 1, 6, 9, 5, 4, 3, 2, 8,
              5, 3, 8, 2, 1, 7, 4, 9, 6,
              2, 7, 3, 1, 6, 9, 8, 4, 5,
              8, 5, 9, 4, 7, 3, 1, 6, 2,
              4, 6, 1, 8, 2, 5, 9, 3, 7,
              6, 4, 7, 3, 8, 2, 5, 1, 9,
              3, 8, 2, 5, 9, 1, 6, 7, 4,
              1, 9, 5, 7, 4, 6, 2, 8, 3]
    s = Sudoku(solved, unsolved)
    return s

'''
easy erstellt ein einfaches Sudoku
'''
def easy():
    unsolved = [6, 3, "", "", 9, "", "", 2, 8,
                "", 4, "", 7, "", 8, "", 1, "",
                "", "", "", 3, "", 4, "", "", "",
                "", "", 3, "", "", "", 5, "", "",
                "", "", "", 8, "", 6, "", "", "",
                "", 5, 6, "", "", "", 7, 8, "",
                8, "", "", "", "", "", "", "", 9,
                "", 1, 4, 6, "", 5, 3, 7, "",
                "", "", "", 9, "", 7, "", "", ""]
    solved = [6, 3, 7, 5, 9, 1, 4, 2, 8,
              5, 4, 9, 7, 2, 8, 6, 1, 3,
              1, 2, 8, 3, 6, 4, 9, 5, 7,
              4, 8, 3, 1, 7, 2, 5, 9, 6,
              7, 9, 1, 8, 5, 6, 2, 3, 4,
              2, 5, 6, 4, 3, 9, 7, 8, 1,
              8, 7, 5, 2, 4, 3, 1, 6, 9,
              9, 1, 4, 6, 8, 5, 3, 7, 2,
              3, 6, 2, 9, 1, 7, 8, 4, 5]
    s = Sudoku(solved, unsolved)
    return s

'''
medium erstellt ein moderates Sudoku
'''
def medium():
    unsolved = [5, 4, "", "", 3, "", "", "", "",
                "", 9, "", "", 7, 1, "", "", "",
                "", "", 2, "", "", 4, 8, "", "",
                "", "", "", "", "", "", 3, 5, "",
                1, 6, "", "", "", "", "", 2, 8,
                "", 3, 4, "", "", "", "", "", "",
                "", "", 9, 7, "", "", 1, "", "",
                "", "", "", 2, 4, "", "", 8, "",
                "", "", "", "", 6, "", "", 3, 9]
    solved = [5, 4, 1, 8, 3, 2, 9, 7, 6,
              8, 9, 3, 6, 7, 1, 5, 4, 2,
              6, 7, 2, 9, 5, 4, 8, 1, 3,
              9, 2, 8, 4, 1, 6, 3, 5, 7,
              1, 6, 5, 3, 9, 7, 4, 2, 8,
              7, 3, 4, 5, 2, 8, 6, 9, 1,
              2, 5, 9, 7, 8, 3, 1, 6, 4,
              3, 1, 6, 2, 4, 9, 7, 8, 5,
              4, 8, 7, 1, 6, 5, 2, 3, 9]
    s = Sudoku(solved, unsolved)
    return s

'''
hard erstellt ein schweres Sudoku
'''
def hard():
    unsolved = [9, 2, "", "", "", "", 8, "", "",
                "", "", "", "", "", 9, "", 7, "",
                "", "", "", "", 1, 5, 6, 9, 2,
                "", "", "", 6, 8, "", "", "", "",
                "", "", 1, "", 4, "", "", 8, 6,
                "", "", "", 9, 5, "", "", "", 1,
                3, 9, 6, 5, 7, "", "", "", "",
                "", 5, "", 3, "", "", "", "", 7,
                "", "", 8, "", "", "", "", 5, ""]
    solved = [9, 2, 5, 7, 3, 6, 8, 1, 4,
              6, 1, 4, 8, 2, 9, 5, 7, 3,
              7, 8, 3, 4, 1, 5, 6, 9, 2,
              2, 4, 9, 6, 8, 1, 7, 3, 5,
              5, 3, 1, 2, 4, 7, 9, 8, 6,
              8, 6, 7, 9, 5, 3, 2, 4, 1,
              3, 9, 6, 5, 7, 4, 1, 2, 8,
              1, 5, 2, 3, 9, 8, 4, 6, 7,
              4, 7, 8, 1, 6, 2, 3, 5, 9]
    s = Sudoku(solved, unsolved)
    return s

'''
expert erstellt ein sehr schweres Sudoku
'''
def expert():
    unsolved = ["", "", 1, 3, 6, 4, 8, "", "",
                7, "", "", "", "", "", "", "", "",
                "", "", "", 7, 1, 2, "", "", "",
                "", "", 6, "", "", "", 4, "", "",
                "", 5, "", "", 4, "", "", 8, "",
                "", 2, "", "", 5, "", "", 3, "",
                "", "", 5, "", "", "", 9, "", "",
                6, "", "", 1, 3, 9, "", "", 8,
                3, 7, "", "", "", "", "", 2, 6]
    solved = [2, 9, 1, 3, 6, 4, 8, 5, 7,
              7, 3, 4, 5, 9, 8, 2, 6, 1,
              5, 6, 8, 7, 1, 2, 3, 9, 4,
              9, 8, 6, 2, 7, 3, 4, 1, 5,
              1, 5, 3, 9, 4, 6, 7, 8, 2,
              4, 2, 7, 8, 5, 1, 6, 3, 9,
              8, 1, 5, 6, 2, 7, 9, 4, 3,
              6, 4, 2, 1, 3, 9, 5, 7, 8,
              3, 7, 9, 4, 8, 5, 1, 2, 6]
    s = Sudoku(solved, unsolved)
    return s
