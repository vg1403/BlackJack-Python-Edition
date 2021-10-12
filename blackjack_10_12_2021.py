#This game is called blackjack
import random
deck=["Hearts Ace","Hearts 2","Hearts 3","Hearts 4","Hearts 5","Hearts 6","Hearts 7","Hearts 8","Hearts 9","Hearts 10","Hearts King","Hearts Queen","Hearts Jack","Diamonds Ace","Diamonds 2","Diamonds 3","Diamonds 4","Diamonds 5","Diamonds 6","Diamonds 7","Diamonds 8","Diamonds 9","Diamonds 10","Diamonds King","Diamonds Queen","Diamonds Jack","Clubs Ace","Clubs 2","Clubs 3","Clubs 4","Clubs 5","Clubs 6","Clubs 7","Clubs 8","Clubs 9","Clubs 10","Clubs King","Clubs Queen","Clubs Jack","Spades Ace","Spades 2","Spades 3","Spades 4","Spades 5","Spades 6","Spades 7","Spades 8","Spades 9","Spades 10","Spades King","Spades Queen","Spades Jack"]
deckCopy=[]
shuffled=[]
playerInput=input("Do You want to Play BlackJack? Y/N")
computerDeck=[]
playerDeck=[]
def daRules():
        print("Rule 1. Each player recieves two cards in which one is hidden and the other is not hidden")
        print("Rule 2. Each player can ask for a card (a.k.a a hit) from the deck")
        print("Rule 3. The player's cards can have a total value over 21 or they lose.")
        print("Rule 4. The player cards can have the ability to look at the other face up cards.")
def counter(player):
        counter = 0;
        for x in range(player.length):
                if("Ace" in player[x]):
                        if(counter==10):
                                counter=21
                        else:
                                counter+=1
                if("2" in player[x]):
                        counter+=2
                if("3" in player[x]):
                        counter+=3
                if("4" in player[x]):
                        counter+=4
                if("5" in player[x]):
                        counter+=5
                if("6" in player[x]):
                        counter+=6
                if("7" in player[x]):
                        counter+=7
                if("8" in player[x]):
                        counter+=8
                if("9" in player[x]):
                        counter+=9
                if("10" in player[x]):
                        if(counter==1):
                                counter=21
                        else:
                                counter+=10
                if("King" in player[x]):
                        if(counter==1):
                                counter=21
                        else:
                                counter+=10
                if("Queen" in player[x]):
                        if(counter==1):
                                counter=21
                        else:
                                counter+=10
                if("Jack" in player[x]):
                        if(counter==1):
                                counter=21
                        else:
                                counter+=10
        if(counter<21):
                return counter
        elif(counter>21):
                return "Bust"
        else:
                return "BlackJack"
def shuffle():
        x=51
        while(x>=0):
                n=random.randint(0,x)
                shuffled.append(deckCopy[n])
                deckCopy.pop(n)
                x-=1
def copyDeck():
        for x in range(len(deck)):
                deckCopy.append(deck[x])       
        
def deal(player):
        player.append(shuffled.pop(0))
        player.append(shuffled.pop(0))

def showCards(player):
        for x in range(len(player)):
                print(player[x])
def hit(player):
        player.append(shuffled.pop(0))
        
if(playerInput=="Y"):
        while(playerInput!="N"):
                copyDeck()
                playIn=input("Do you want to see the rules? Y/N")
                while(playIn!="N"):
                        if(playIn=="Y"):
                                daRules();
                                playIn=input("Do You want to still see the rules? Y/N")
                        if(playIn!="Y") or (playIn!="N"):
                                playIn=input("Please select either Y or N")
                shuffle()
                print("Dealing cards")
                
                deal(playerDeck)
                
                deal(computerDeck)
                
                print("Player's Deck:")
                showCards(playerDeck)

                hitOrStand=""
                while(hitOrStand=="" or hitOrStand=="hit"):
                        hitinput("Do you want to hit or stand?")
                        if(hitOrStand=="hit"):
                                hit(playerDeck)
                                counter(playerDeck)
                                computerChoice= random.randint(0,1)
                                if(computerChoice==0):
                                        hit(computerDeck)
                                else:
                                        stand(computerDeck)
                                
                        elif(hitOrStand=="stand"):
                                stand(playerDeck)
                        else:
                                hitOrStand=""
                                        
else:
        quit()
