
print('HELLO GAMERS WELCOME TO MY WONDERFUL WORLD OF ADVENTURE GAME:')
print()
import time
#this get input from the user
options= input('Do you wanna play the game? (YES/NO): ')
print()


if options.lower() == 'no':
    time.sleep(2)
    print('Thanks for trying out our game see you next time') 

if options.lower() == 'yes': 
    time.sleep(2)
    answer = input('You pick up the match and strike it, and for an instant, the forest around you is illuminated. You see a large grizzly bear, and then the match burns out. Do you want to RUN, PLAY-DEAD, or HIDE behind a tree? ')
    if answer.lower() == 'run':
        time.sleep(2)
        answer = input('oops! the bear is relentless and you got to a junction, will you turn WEST, EAST or SOUTH? ')
        if answer.lower() == 'west':
            time.sleep(2)
            print('Congratulations!!! you have gotten to a safe zone,and you have successfully escaped the bear. you have won')

        if answer.lower() == 'east':
            time.sleep(2)
            print('You got stucked and buried in a sinking sand, you are dead. GAME OVER!')
        if answer.lower() == 'south':
            time.sleep(2)
            print('The south is the current position of the Bear, you have been killed. GAME OVER!')
    
    if answer.lower() == 'play-dead':
        time.sleep(2)
        answer = input('The bear comes over to where you played dead, will you MOVE, BREATHE-HEAVILY OR BE-STILL?  ')
        if answer.lower() == 'move':
            time.sleep(2)
            print('ouch!!! you have been killed, you lost. GAME OVER!')

        if answer.lower() == 'breathe-heavily':
            time.sleep(2)
            print('Sorry, you got killed by the bear. you are dead. GAME OVER!')
        if answer.lower() == 'be-still':
            time.sleep(2)
            print('Congratulations!!! you won the game. WINNER!!!')
    
    if answer.lower() == 'hide':
        time.sleep(2)
        answer = input('oops! luckily for you the bear noticed you from 300fts, will you wait to ATTACK, RETREAT-SLOWLY or SCREAM? ')
        if answer.lower() == 'attack':
            time.sleep(2)
            print('OH Mhen!! the bear over-powered you and you were crushed. GAME OVER!!')

        if answer.lower() == 'retreat-slowly':
            time.sleep(2)
            print('Congratulations!!! you are safe, you won. WINNER!!!!!!!!')
        if answer.lower() == 'scream':
            time.sleep(2)
            print('The bear saw you as threat and possible meal. you have been killed. GAME OVER!')  
        else:
            print('Sorry that was an invalid option Game over please try again')    
    else:
            print('Sorry that was an invalid option Game over please try again')    
else:
    print('Wrong choice please reply with YES/NO next time GAME OVER!!')
        
        