import random
l=['rock','paper','scissor']

while True:
    uscore=0
    cscore=0
    uc=int(input('''
                 
     Game start.....
           1 Yes = game start
           2 No = Exit      
                 
                 '''))
    
    if uc==1:
        
        
        for a in range(1,6):
            
            
            user_input=int(input('''
                         
            1 Rock
            2 Paper
            3 scissor                     
                                 '''))
            
            if user_input==1:
               ucchose='rock'
            elif user_input==2:
                ucchose='paper'
            elif user_input==3:
                ucchose='scissor'
                
            cchose=random.choice(l)
            
            if ucchose==cchose:
                print('computer choice',cchose)
                print('user choice',ucchose)
                print('The game is draw--:<')  
                uscore=uscore+1
                cscore=cscore+1
                
            elif (ucchose=="rock" and cchose=='scissor') or (ucchose=='paper' and cchose=="rock") or (ucchose=='scissor' and cchose=='paper'):             
                print('computer choice',cchose)
                print('user choice',ucchose)
                print("you win this round-- :)")
                uscore=uscore+1
                 
            else:
                print('computer choice',cchose)
                print('user choice',ucchose)
                print('you lost this round-- :(')      
                cscore=cscore+1


                
        if uscore==cscore:
            print('uscore:',uscore)    
            print('cscore:',cscore)  
            print('this game is draw')
        elif uscore>cscore:
            print('uscore:',uscore)    
            print('cscore:',cscore)  
            print("you win the game")
        else:
            print('uscore:',uscore)    
            print('cscore:',cscore) 
            print('you lost the game')     
                  
        
        
            
    else:
        break
    
        
        