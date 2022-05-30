import tkinter as tk
from tkinter import ttk
import sudokus

###############################################################################
#   Main Funktion   ###########################################################
###############################################################################

if __name__ == '__main__':

    '''
    main_menu erstellt das Hauptmenü.
    '''
    def main_menu():

        #######################################################################
        #   GUI Einrichten   ##################################################
        #######################################################################

        root = tk.Tk()
        root.title("Hauptmenü")
        root.geometry("295x320+120+120")

        print("--- rot set ---")

        #######################################################################
        #   Funktionen   ######################################################
        #######################################################################

        '''
        start_game schließt das Hauptmenü und ruft entsprechend der 
        Nutzerauswahl ein neues Spiel auf.
        '''
        def start_game(difficulty):
            if difficulty == "beginner":
                title = "ANFÄNGER"
                sudoku = sudokus.beginner()
            elif difficulty == "easy":
                title = "EINFACH"
                sudoku = sudokus.easy()
            elif difficulty == "medium":
                title = "MITTEL"
                sudoku = sudokus.medium()
            elif difficulty == "hard":
                title = "SCHWER"
                sudoku = sudokus.hard()
            else:
                title = "EXPERTE"
                sudoku = sudokus.expert()
            root.destroy()
            new_game(sudoku, title)

        '''
        event_how_to schließt das Hauptmenü und ruft die Spielanleitung auf.
        '''
        def event_how_to():
            root.destroy()
            how_to_play()

        '''
        event_close schließt die Anwendung.
        '''
        def event_close():
            print("\nevent_close()")
            print("--- ending game ---")
            root.destroy()

        print("--- start-methods set ---")


        #######################################################################
        #   Labels & Buttons   ################################################
        #######################################################################

        headline = ttk.Label(root, text="SUDOKU", justify=tk.CENTER,
                             font="Verdana 30")
        headline.pack()

        subline = ttk.Label(root, text="""
Wähle einen Schwierigkeitsgrad:
""", justify=tk.CENTER)
        subline.pack()

        print("--- labels set ---")

        beginner_b = ttk.Button(root, text="Anfänger",
                                command=lambda: start_game("beginner"))
        beginner_b.pack()

        easy_b = ttk.Button(root, text="Einfach",
                            command=lambda: start_game("easy"))
        easy_b.pack()

        medium_b = ttk.Button(root, text="Mittel",
                              command=lambda: start_game("medium"))
        medium_b.pack()

        hard_b = ttk.Button(root, text="Schwer",
                            command=lambda: start_game("hard"))
        hard_b.pack()

        expert_b = ttk.Button(root, text="Experte",
                              command=lambda: start_game("expert"))
        expert_b.pack()

        how_to_play_b = ttk.Button(root, text="Wie wird gespielt?",
                                   command=event_how_to)
        how_to_play_b.pack()

        close_b = ttk.Button(root, text="Beenden", command=event_close)
        close_b.pack()

        print("--- buttons set ---")

        #######################################################################
        #   GUI Starten   #####################################################
        #######################################################################

        root.mainloop()

    '''
    new_game erstellt eine GUI für das aktuelle Sudoku-Spiel
    '''
    def new_game(sudoku, difficulty):

        #######################################################################
        #   GUI Einrichten   ##################################################
        #######################################################################

        game = tk.Tk()
        game.title(difficulty)
        game.geometry("295x320+120+120")
        game.resizable(width=False, height=False)
        error_txt = tk.StringVar()
        error_txt.set("")


        #######################################################################
        #   Funktionen   ######################################################
        #######################################################################

        '''
        update wird durch KeyRelease-Event ausgelöst. Die Funktion überprüft,
        in welchem Feld eine Interaktion stattgefunden hat und übernimmt den
        geänderten Wert in das aktuelle Sudoku.
        '''
        def update(*args):
            print("\nKeyRelease -> update()")
            for a in range(81):
                if entry_fields[a].get() != "":
                    if sudoku.in_progress[a] != int(entry_fields[a].get()):
                        print("--- updating cell", a, "- value:",
                              entry_fields[a].get(), "---")
                        sudoku.in_progress[a] = int(entry_fields[a].get())
                if entry_fields[a].get() == "":
                    sudoku.in_progress[a] = ""
            if sudoku.check_full() and not sudoku.find_error():
                finalize()

        '''
        validate sorgt dafür, dass nur Ziffern von 0-9 in die Felder
        eingetragen werden können.
        '''
        def validate(user_input):
            if len(user_input) == 0:
                return True
            elif len(user_input) == 1 and user_input.isdigit():
                return True
            else:
                return False

        vcmd = (game.register(validate), '%P')

        '''
        event_close wird durch den Button "beenden" ausgelöst.
        Die Funktion schließt die Anwendung.
        '''
        def event_close():
            print("\nevent_close()")
            print("--- ending game ---")
            game.destroy()

        '''
        event_menu wird durch den "Menü" Button ausgelöst.
        Die Funktion schließt das aktuelle spiel und öffnet das Hauptmenü.
        '''
        def event_menu():
            print("\nevent_menu()")
            game.destroy()
            main_menu()

        '''
        event_hint wird durch den "Hinweis" Button ausgelöst.
        Die Funktion prüft das aktuelle Sudoku auf Fehler.
        Wird ein Fehler gefunden, wird ein entsprechendes Label eingeblendet.
        Wird kein Fehler gefunden, wird ein zufälliges Feld gelöst.
        '''
        def event_hint():
            print("\nevent_hint()")
            if not sudoku.find_error():
                error_txt.set("")
                hint_index = sudoku.hint()
                entry_fields[hint_index].insert("",
                                                sudoku.in_progress[hint_index])
                if sudoku.check_full():
                    finalize()
            else:
                error_txt.set("Fehler gefunden")

        '''
        finalize blendet einen Hinweis ein, wenn das Sudoku korrekt gelöst 
        wurde.
        '''
        def finalize():
            print("\nfinalize()")
            c_final = tk.Canvas(game)
            c_final.config(width=100, height=60, background="green")
            c_final.create_text(50, 30, text="Gewonnen", fill="white",
                                anchor=tk.CENTER)
            c_final.place(x=145, y=125, anchor=tk.CENTER)

        #######################################################################
        #   Raster   ##########################################################
        #######################################################################

        c = tk.Canvas(game)
        c.config(width=295, height=290)
        c.create_line(0, 80, 290, 80)
        c.create_line(0, 165, 290, 165)
        c.create_line(95, 0, 95, 245)
        c.create_line(195, 0, 195, 245)
        c.place(x=0, y=0)


        #######################################################################
        #   Eingabefelder   ###################################################
        #######################################################################

        entry_fields = []

        entry_style = ttk.Style()
        entry_style.configure("EntryStyle.TEntry", background='black')
        entry_style.map("EntryStyle.TEntry",
                        foreground=[('disabled', 'black'),
                                    ('!disabled', 'blue')],
                        background=[('disabled', 'lightgrey'),
                                    ('!disabled', 'white')])

        for i in range(81):
            entry_fields.append(ttk.Entry(game, validate="key",
                validatecommand=vcmd, width=2, justify=tk.CENTER,
                style="EntryStyle.TEntry"))
            entry_fields[i].insert("", sudoku.in_progress[i])
            if sudoku.unsolved[i] != "":
                entry_fields[i].config(state='disabled', background="")
            else:
                entry_fields[i].bind("<KeyRelease>", update)

            x = 0
            y = 0

            if 18 > i > 8:
                y = 25
            elif 27 > i > 17:
                y = 50
            elif 36 > i > 26:
                y = 85
            elif 45 > i > 35:
                y = 110
            elif 54 > i > 44:
                y = 135
            elif 63 > i > 53:
                y = 170
            elif 72 > i > 62:
                y = 195
            elif 81 > i > 71:
                y = 220

            if (i + 8) % 9 == 0:
                x = 30
            elif (i + 7) % 9 == 0:
                x = 60
            elif (i + 6) % 9 == 0:
                x = 100
            elif (i + 5) % 9 == 0:
                x = 130
            elif (i + 4) % 9 == 0:
                x = 160
            elif (i + 3) % 9 == 0:
                x = 200
            elif (i + 2) % 9 == 0:
                x = 230
            elif (i + 1) % 9 == 0:
                x = 260

            entry_fields[i].place(x=x, y=y)


        #######################################################################
        #   Error Hint   ######################################################
        #######################################################################

        error_l = ttk.Label(game, textvariable=error_txt)
        error_l.place(x=145, y=265, anchor=tk.CENTER)


        #######################################################################
        #   Buttons   #########################################################
        #######################################################################

        hint_b = ttk.Button(game, text="Hinweis", command=event_hint)
        hint_b.config(width=6)
        hint_b.place(x=0, y=280, anchor=tk.NW)

        menu_b = ttk.Button(game, text="Menü", command=event_menu)
        menu_b.config(width=6)
        menu_b.place(x=100, y=280, anchor=tk.NW)

        close_b = ttk.Button(game, text="Beenden", command=event_close)
        close_b.config(width=6)
        close_b.place(x=200, y=280, anchor=tk.NW)


        #######################################################################
        #   GUI starten   #####################################################
        #######################################################################

        game.mainloop()

    '''
    how_to_play erstellt eine GUI für die Spielanleitung.
    '''
    def how_to_play():

        #######################################################################
        #   GUI Einrichten   ##################################################
        #######################################################################

        info = tk.Tk()
        info.title("Wie wird gespielt?")
        info.geometry("295x320+120+120")

        #######################################################################
        #   Funktionen   ######################################################
        #######################################################################

        '''
        event_menu wird durch den "Zurück" Button ausgelöst.
        Die Funktion schließt die aktuelle GUI und öffnet das Menü.
        '''
        def event_menu():
            print("\nevent_menu()")
            info.destroy()
            main_menu()

        #######################################################################
        #   Labels & Buttons   ################################################
        #######################################################################

        header_l = ttk.Label(info, text="Anleitung", justify=tk.CENTER,
                             font="Verdana 30")
        header_l.pack()

        how_to_l = ttk.Label(info, text="""
In jede Zelle des 9x9-Rasters
kommt eine Zahl von 1 bis 9.
        
Dabei darf jede Zahl nur einmal
pro Zeile, pro Spalte und pro
3x3-Raster vorkommen.
        
Ein Klick auf 'Hinweis' löst eine
zufällige Zelle oder zeigt dir an,
wenn dein Sudoku einen Fehler 
enthält.
""", justify=tk.CENTER)

        how_to_l.pack()

        back_b = ttk.Button(info, text="Zurück", command=event_menu)
        back_b.pack()

    main_menu()
