"""

@author: Akshay-G-Dev

@title: Tic Tac Toe

!!Do Not Copy!!

Thank You!

:)

🙃🙃🙃🙃🙃🙃🙃

"""

moves=[['     ' for i in range(3)]for j in range(3)]

movesPlay=[11,12,13,21,22,23,31,32,33]

Xcount=0

Ocount=0

print('PLAYER 1: ❎\nPLAYER 2: 🅾️')

a=0

player,turn=1,'❎'

while True:

    

    print(f'''

  row>   1     2     3

      {'_'*20}

 c  1 |{moves[0][0]}|{moves[1][0]}|{moves[2][0]}|

 o    -------------------

 l  2 |{moves[0][1]}|{moves[1][1]}|{moves[2][1]}|

 u    -------------------   

 m  3 |{moves[0][2]}|{moves[1][2]}|{moves[2][2]}|

 n    {'_'*20}

      ''')

    

    

    if (moves[0][0]==moves[1][0]==moves[2][0]!='     ' or moves[0][1]==moves[1][1]==moves[2][1]!='     ' or moves[0][2]==moves[1][2]==moves[2][2]!='     ' or moves[0][0]==moves[0][1]==moves[0][2]!='     ' or moves[1][0]==moves[1][1]==moves[1][2]!='     ' or moves[2][0]==moves[2][1]==moves[2][2]!='     ' or moves[0][0]==moves[1][1]==moves[2][2]!='     ' or moves[2][0]==moves[1][1]==moves[0][2]!='     '):

        if Xcount>Ocount:

            print('Player 1(❎) won')

        else:

            print('Player 2(🅾️) won')

        break

    if ((Xcount==4 and Ocount==5) or(Xcount==5 and Ocount==4)):

        print('Draw match')

        break

    

    

    

    user=input(f'Player {player}({turn}) turn (11,12,..):')

    

    try:

        if not(int(user) in movesPlay):

            print('This move is already played or invalid move, try another move')

            continue

        i1=list(user)

        if player==1:

            moves[int(i1[0])-1][int(i1[1])-1]=turn.center(4)

        else:

            moves[int(i1[0])-1][int(i1[1])-1]=turn.center(5)

        movesPlay.remove(int(user))

        if turn=='❎':

            Xcount+=1

            print(Xcount,Ocount)

        else:

            Ocount+=1

    except:

        print(f"Wrong Input!\n{''.join(i1)} is not defined.")

        continue

    if player==1:

        player=2

        turn='🅾️'

    elif player==2:

        player=1

        turn='❎'

        

    
