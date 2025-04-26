def hangman(word):
    wrong = 0
    stages = ["",
               "________       ",
               "|              ",
               "|       |      ",
               "|       0      ",
               "|     / | \    ",
               "|      / \     ",
               "|              "
               ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Welcome to the murder")
    
    while wrong < len(stages) - 1:
        print("\n")
    
        msg = "Guess the letter: "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong+=1
        print(("".join(board)))
        e = wrong + 1
        print("\n".join(stages[0, e]))
        if "__" not in board:
            print("You win! The hiddeb word was: ")
            print("".join(board))
            win = True
            break        
    