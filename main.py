import random 
from art import logo

def blackjack():

  print(logo)
  print("Welcome to BlackJack")
  
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  
  def new_card(hand,score):
    card=cards[random.randint(0,12)]
    hand.append(card)
    for i in range(0,len(hand)-1):
      if hand[i]==11 and score+card>21:
        hand[i]=1
        print(hand)
  
  player_hand=[]
  computer_hand=[]
  
  for i in range (0,2):
    new_card(player_hand,0)
    new_card(computer_hand,0)
  
  print("Dealer's first card is: ",computer_hand[0])
  ask_card="y"
  while ask_card=="y":
    
    print("Your hand is: ",player_hand)
    player_score=sum(player_hand)
    print("Your total score is:", player_score)
    if player_score <= 21:
      ask_card=input("Do you want a card? Type 'y' or 'n' ").lower()
    else:
      ask_card="n"
    if ask_card=="y":
      new_card(player_hand,player_score)
  
  print("Dealer's starting hand is: ", computer_hand)
  computer_score=sum(computer_hand)
  print("Dealer's starting score is: ",computer_score)
  
  end_game=False
  while end_game==False:
    if computer_score <= 21:
      print("Dealer's hand is: ", computer_hand)
      print("Dealer's score is: ",computer_score)
      if player_score>21:
        print("Dealer wins")
        end_game=True
      elif computer_score<player_score:
        new_card(computer_hand,computer_score)
        computer_score=sum(computer_hand)
      elif computer_score==player_score and player_score>16:
        print("It's Tie")
        end_game=True
      elif computer_score==player_score and player_score<=16:
         new_card(computer_hand)
         computer_score=sum(computer_hand,computer_score)  
      else:
        print("Dealer Wins")
        end_game=True
      
    if computer_score>21:
      print("Dealer's hand is: ", computer_hand)
      print("Dealer's score is: ",computer_score)
      print("You win")
      end_game=True
  

  restart_game=input("Do you  want to restart game? Type 'y' or 'n'").lower()
  if restart_game=="y":
    blackjack()
  
blackjack()
