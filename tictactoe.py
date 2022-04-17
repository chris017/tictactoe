# spielfeld und mögliche gewinner züge fesgelegt
# Main Methode ist tic_tac_toe()

def main() -> None:
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    end = False
    win_commbinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
 
    # Das Spielfeld ausgeben
    def draw() -> None:
        print(f'{board[0]} | {board[1]} | {board[2]}')
        print(f'{board[3]} | {board[4]} | {board[5]}')
        print(f'{board[6]} | {board[7]} | {board[8]}')
        print()
 
    # Spieler 1 auswahl von spielzug
    def p1() -> None:
        n = choose_number()
    # Überprüfung ob schon belegt
        if board[n] == "X" or board[n] == "O":
            print("\nYou can't go there. Try again")
            p1()
        else:
            board[n] = "X"
    
    # Spieler 2 auswahl von spielzug
    def p2() -> None:
        n = choose_number()
    # Überprüfung ob schon belegt
        if board[n] == "X" or board[n] == "O":
            print("\nYou can't go there. Try again")
            p1()
        else:
            board[n] = "O"
 
    def choose_number() -> int:
        while True:
            while True:
                a = input()
                # tests the block for errors in the code
                try:
                # input -1 wegen 0-9
                    a = int(a)
                    a -= 1
                    if a in range(0, 9):
                        return a
                    else:
                    # Überprüfung ob zahl auf dem spielfeld existiert
                        print("\nThat's not on the board. Try again")
                        continue
                        # überprüfung ob es überhaupt eine Zahl ist
                        # wenn es keine Zahl ist dann den value error akzeptieren und print ausgeben
                except ValueError:
                    print("\nThat's not a number. Try again")
                    continue
    
    def check_board() -> bool:
        # counter festlegen und auf null setzen
        count = 0
        # Gewinner zuüge abfragen und Gratulieren
        for a in win_commbinations:
            if board[a[0]] == board[a[1]] == board[a[2]] == "X":
                print("Player 1 Wins!\n")
                print("Congratulations!\n")
                return True

            if board[a[0]] == board[a[1]] == board[a[2]] == "O":
                print("Player 2 Wins!\n")
                print("Congratulations!\n")
                return True

        for a in range(9):
            if board[a] == "X" or board[a] == "O":
            # immer plus 1 zählen und damit den counter erhöhen
                count += 1
            if count == 9:
                # falls der count bei 9 ist ist das Spiel unentschieden
                print("The game ends in a Tie\n")
                return True
 
    # solange end nicht erreicht ist continue und ausgabe von spielfeld
    while not end:
        draw()
        end = check_board()
        if end:
            break
        # Input von User für Player 1
        print("Player 1 choose where to place a cross. Choose a Number between 1 and 9: ")
        p1()
        print()
        draw()
        end = check_board()
        if end:
            break
        # Input von User für Player 1
        print("Player 1 choose where to place a cross. Choose a Number between 1 and 9: ")
        p2()
        print()
        # Abfrage ob nochmal gespielt werden soll
    if input("Play again (y/n)\n") == "y":
        print()
        # restart durch erneute abfrage der main methode in dem Fall tic_tac_toe() auserhalb der while Schleife
        main()
    else:
        print('Bye thanks for playing')

if __name__ == "__main__":
    main()