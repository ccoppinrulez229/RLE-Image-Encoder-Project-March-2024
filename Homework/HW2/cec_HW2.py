from p1_random import P1Random
rng = P1Random()

#variables to be used throughout the game
gamestarted=1
game=1
playerwins=0
dealerwins=0
ties=0
hand=0
totalgames=0

while True:
    if gamestarted==1:
        print("\nSTART GAME #",game,sep='')
    card = rng.next_int(13) + 1 #generates fixed number from 1-13 from imported file for player's card
    if card==1 or card>=11: #determines which card to display to user
        if card==1:
            print("\nYour card is a ACE!")
        if card==11:
            print("\nYour card is a JACK!")
        if card==12:
                print("\nYour card is a QUEEN!")
        if card==13:
            print("\nYour card is a KING!")
    else:
        print("\nYour card is a ",card,"!",sep='')
    if card<=10: #determines what value card to add to the hand
        hand=hand+card
    else:
        hand=hand+10
    print("Your hand is:", hand)
    if hand==21: #automatically displays player win if hand is 21, starting a new loop and resetting values
        print("\nBLACKJACK! You win!")
        playerwins+=1
        gamestarted=1
        hand=0
        game+=1
        totalgames += 1
        continue
    if hand>21: #automatically displays dealer win if hand is 21, starting a new loop and resetting values
        print("\nYou exceeded 21! You lose.")
        dealerwins+=1
        gamestarted=1
        hand=0
        game+=1
        totalgames += 1
        continue
    print("\n1. Get another card\n2. Hold hand\n3. Print statistics\n4. Exit")
    option=int(input("\nChoose an option: "))
    while option<1 or option>4: #if an option that's not 1-4 is selected, invalid option will be displayed until correct option is chosen
        print("\nInvalid input!\nPlease enter an integer value between 1 and 4.")
        print("\n1. Get another card\n2. Hold hand\n3. Print statistics\n4. Exit")
        option = int(input("\nChoose an option: "))
    while option==3: #with option 3 selected, stats will continue to be displayed to the user until they select a different option
        winpercent=(playerwins/totalgames)*100
        winpercent=round(winpercent,1)
        print("\nNumber of Player wins: ",playerwins,"\nNumber of Dealer wins: ",dealerwins,"\nNumber of tie games: ",ties,"\nTotal # of games played is: ",totalgames)
        print("Percentage of Player wins: ",winpercent,"%",sep='')
        print("\n1. Get another card\n2. Hold hand\n3. Print statistics\n4. Exit")
        option = int(input("\nChoose an option: "))
    if option==2: #with option 2 selected, randomly generates dealer's hand from 16-26 to determine the winner
        dealerhand = rng.next_int(11) + 16
        print("\nDealer's hand: ",dealerhand)
        print("Your hand is: ",hand)
        if hand==dealerhand: #displays if there is a tie
            print("\nIt's a tie! No one wins!")
            gamestarted=1
            hand=0
            game+=1
            ties+=1
            totalgames += 1
            continue
        if dealerhand>21: #displays if the dealer exceeds a hand of 21. player wins
            print("\nYou win!")
            playerwins+=1
            gamestarted=1
            hand=0
            game+=1
            totalgames += 1
            continue
        if dealerhand==21: #displays if dealer has a hand of 21. dealer wins
            print("\nDealer wins!")
            dealerwins += 1
            gamestarted = 1
            hand = 0
            game += 1
            totalgames += 1
            continue
        if dealerhand<21: #determines who's closer to 21 when dealer has a hand less than 21
            if hand>dealerhand:
                print("\nYou win!")
                playerwins+=1
                gamestarted=1
                hand=0
                game+=1
                totalgames += 1
                continue
            if hand<dealerhand:
                print("\nDealer wins!")
                dealerwins+=1
                gamestarted=1
                hand=0
                game+=1
                totalgames += 1
                continue
    if option==1: #with option 1 selected, gamestarted variable will be set to 0 so "STARTGAME" text isnt displayed and loop will begin again choosing another number
        gamestarted=0
    if option==4: #with option 4 selected, program is exited
        break