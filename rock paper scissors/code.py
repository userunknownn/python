import random 

def playGame():
    
    acceptableChoices = ['r','p','s']
    userChoice        = ''
  
    while True:  
        userChoice    = input("'r' for rock, 'p' for paper, 's' for scissors : ")
        
        if userChoice in acceptableChoices:
            break
        else:
            print(f"Your choice '{userChoice}' is an invalid one!")
    
    computerChoice    = random.choice(['r','p','s'])
    
    print(f"Computer choice was : {computerChoice}")
    print(f"User choice was     : {userChoice}")

    
    if userChoice == computerChoice : 
        print("It was a tie")
    else: 
        if userChoice == 'p':
            if computerChoice == 'r':
                print("User wins")
            else: 
                print("Computer wins")
        elif userChoice == 'r':
            if computerChoice == 's':
                print("User wins")
            else: 
                print("Computer wins")
        else:
            if computerChoice == 'p':
                print("User wins")
            else:
                print("Computer wins")
    
playGame()
