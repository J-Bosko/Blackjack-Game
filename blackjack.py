import random
cards=['A','A','A','A',2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,'J','J','J','J','Q','Q','Q','Q','K','K','K','K']

def blackjack():
    print("Lets see if you are good enough!")
    cont = True
    cont_mana=True
    mycards=[]
    manacards=[]
    player=0
    mana=0
    pick1=random.choice(cards)
    cards.remove(pick1)
    mycards.append(pick1)
    if pick1=='A':
        balander=int(input("Wanna consider the A as 1 or 11? "))
        pick1=balander
    if pick1=='J' or pick1=='Q' or pick1=='K':
        pick1=10
    player+=pick1
    
    pick2=random.choice(cards)
    cards.remove(pick2)
    mycards.append(pick2)
    if pick2=='A':
        balander=int(input("Wanna consider the A as 1 or 11? "))
        pick2=balander
    if pick2=='J' or pick2=='Q' or pick2=='K':
        pick2=10
    player+=pick2
    print(f"Your cards after the 1st deal {mycards}. Your total so far: {player}")
    
    pickmana=random.choice(cards)
    cards.remove(pickmana)
    manacards.append(pickmana)
    if pickmana=='A':
        balander=random.choice([11,1])
        pickmana=balander
    if pickmana=='J' or pickmana=='Q' or pickmana=='K':
        pickmana=10
    mana+=pickmana
    print(f"Mana's cards after the 1st deal {manacards}. Mana's so far: {pickmana}")

    if(player==21):
        print("Congrats, you WINNN!!")
        return 0

    while(cont):
        cont=input("Wanna pick another card? If yes type True: ")
        if(cont != 'True'):
            break
        next_pick=random.choice(cards)
        cards.remove(next_pick)
        mycards.append(next_pick)
        if next_pick=='A':
            balander=int(input("Wanna consider the A as 1 or 11? "))
            next_pick=balander
        if next_pick=='J' or next_pick=='Q' or next_pick=='K':
            next_pick=10
        player+=next_pick
        if (player>21):
            print(f"Unfortunately you lost as you exceeded 21. Your sum is {player} and your cards are {mycards}.")
            break
        if(player==21):
            print("Congrats, you WINNN!!")
            return 0
        print(f"Your cards after the deal {mycards}. Your total so far: {player}")
    

    while(cont_mana):
        next_pick_mana=random.choice(cards)
        cards.remove(next_pick_mana)
        mycards.append(next_pick_mana)
        if next_pick_mana=='A':
            balander=random.choice([11,1])
            next_pick_mana=balander
        if next_pick_mana=='J' or next_pick_mana=='Q' or next_pick_mana=='K':
            next_pick_mana=10
        mana+=next_pick_mana

        if (mana>21):
            print(f"It's your lucky day cause mana exceeded 21. Mana's sum is {mana} and your cards are {manacards}.")
            break
        if(mana==21):
            print("Mana has 21, YOU LOSEEEE")
            return 0
        print(f"Mana's cards after the deal {manacards}. Mana's total so far: {mana}")

        if (mana>player and mana<21):
            print("YOU LOSEEEE")
            break

        cont_mana=random.choice(['True','False'])
        if(cont_mana != 'True'):
            break

    if(player>mana and player<21):
        print(f"You WINNNN. Your score was {player} and mana's was {mana}.")
        


blackjack()


